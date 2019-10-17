<template>
  <div>
    <HeaderTop :title="receiverInfo.nickname"></HeaderTop>

    <section id="msg-area">
      <div class="msg-list" ref="chatWrapper">
        <div>

          <div class="msg-item" v-for=" message in messages"
               :class="[message.receiver_id==receiver ? 'msg-item-sender':'msg-item-receiver']">
            <div v-if="message.receiver_id==receiver">
              <img class="avatar"
                   :src="userInfo.avatar"
                   alt="">
            </div>
            <div v-else>
              <img class="avatar"
                   :src="receiverInfo.avatar"
                   alt="">
            </div>

            <div class="message-bubble">
              {{message.body}}
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="send-msg-area">

    </section>
    <footer>
      <i class="icon icon-voice"></i>
      <input type="text" class="text-input" @keyup.enter="sendMsg" v-model="messageBody">
      <i class="icon icon-face"></i>
      <i class="icon icon-plus"></i>

    </footer>
  </div>
</template>

<script>
  import HeaderTop from '../header/HeaderTop'
  import {Checkbox, CheckboxGroup, Button, Toast} from 'vant'
  import {mapState} from 'vuex'
  import BScroll from '@better-scroll/core'
  export default {
    name: 'Chat',
    components: {
      HeaderTop,
      [CheckboxGroup.name]: CheckboxGroup,
      [Checkbox.name]: Checkbox,
      [Button.name]: Button,
      [Toast.name]: Toast,
    },
    data() {
      return {
        messages: [],
        shopCard: {},
        internalId: 0,
        messageBody: '',
        offset: 0,
        receiverInfo: {'avatar': '', 'id': -1}
      }
    },
    methods: {
      //获取对方头像姓名等信息
      getReceiverInfo() {
        let params = {'name': this.receiver}
        this.$api.getUserCard(params).then(res => {
          if (res.code == 1 && res.data) {
            this.receiverInfo = res.data
          }
        })

      },
      //初始化bscroll
      initScroll() {
        this.chatScroll = new BScroll(this.$refs.chatWrapper, {
          click: false,
          bounce:
            {
              top: true,
              bottom: false,
              left: false,
              right: false
            }
        })
        //滚动到底部最新消息处
      },
      initData() {
        if (this.login) {
          this.getReceiverInfo()
        } else {
          this.$router.push('/login')
        }
      },
      async sendMsg() {
        let params = {'receiver': this.receiver, 'body': this.messageBody, 'accessToken': this.accessToken}
        socket.on('connect',()=>{
          console.log(111)
        })

        return
        if (this.messageBody.trim().length > 0) {
          this.$api.sendMessage(params).then(res => {
            if (res.code = 1) {
              this.messageBody = ''
              this.receiveMessages()
            } else {
              this.$toast.fail('发送失败！')
            }
          }).catch(
            res => {
              console.log(res)
            }
          )

        } else {
          this.messageBody = ''
          this.$toast('发送内容不能为空！')

        }

      },
      async receiveMessages() {
        let params = {'receiver': this.receiver, 'accessToken': this.accessToken, 'offset': this.offset}
        this.$api.receiveMessage(params).then(res => {
          if (res.code == 1 & res.data.length > 0) {
            this.messages = res.data
            this.$nextTick((() => {
              this.initScroll()
              this.chatScroll.scrollTo(0, this.chatScroll.maxScrollY)

            }))
          } else {
            console.log(res)
          }
        })

      },
      watchMessage() {
        this.internalId = setInterval(() => {
          setTimeout(this.receiveMessages, 0)
        }, 5000)
      }
    },

    created() {
      this.initData()
    },
    mounted() {
      // this.receiveMessages()
      // this.watchMessage()
    },

    computed: {
      ...mapState(['login', 'accessToken', 'userInfo']),
      receiver() {
        return Number(this.$route.params.receiver)
      },

    },
    beforeDestroy() {
      clearInterval(this.internalId)
    }
  }
</script>

<style scoped lang="scss">

  #msg-area {
    top: 50px;
    bottom: 60px;
    position: absolute;
    width: 100%;
  }

  .msg-list {
    flex: 1;
    overflow: hidden;
    height: 100%;
    width: 100%;
  }

  .msg-item {
    display: flex;
    margin-top: 10px;

    .avatar {
      width: 40px;
      height: 40px;
      margin: 0 10px;
      border-radius: 4px;
    }
  }

  .msg-item-receiver {


    .message-bubble {
      background-color: #fff;

    }

    .message-bubble::before {
      content: '';
      border-top: 1px solid #ddd;
      border-left: 1px solid #ddd;
      width: 10px;
      height: 10px;
      background: #fff;
      position: absolute;
      top: 14px;
      left: -6px;
      transform: rotate(-45deg);
      border-radius: 0 0 20px 0;
    }
  }

  .msg-item-sender {
    flex-direction: row-reverse;

    .message-bubble {
      background-color: #9fe759;
      border-color: #87cd51;
    }

    .message-bubble::before {
      content: '';
      border-top: 1px solid #87cd51;
      border-left: 1px solid #87cd51;
      width: 10px;
      height: 10px;
      background-color: #9fe759;
      position: absolute;
      top: 14px;
      right: -6px;
      transform: rotate(135deg);
      border-radius: 0 0 20px 0;
    }
  }

  .message-bubble {
    border: 1px solid #ddd;
    padding: 7px 10px;
    border-radius: 3px;
    max-width: 70%;
    position: relative;

    word-wrap: break-word;
    word-break: break-all;

  }

  footer {
    position: fixed;
    bottom: 0;
    height: 50px;
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
    background-color: #f5f5f7;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  footer .icon {
    width: 28px;
    height: 28px;
    margin-left: 10px;
  }

  footer .icon:last-child {
    margin-right: 10px;
  }

  footer .text-input {
    flex: 1;
    margin-left: 10px;
    height: 36px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background: #f5f5f5;
  }

  footer .icon-voice {
    background-image: url('../../style/icon/voice.svg');
  }

  footer .icon-plus {
    background-image: url('../../style/icon/plus-cycle.svg');
  }

  footer .icon-face {
    background-image: url('../../style/icon/smile-face.svg');
  }
</style>
