<template>
  <div class="main">
    <div class="head">
      <div class="user-avatar">
        <img :src="comment.userImg" alt="">
      </div>
      <div class="head-main ">
        <div>{{comment.userName}}</div>
        <span>
          {{comment.commentTime}}
        </span>

      </div>
    </div>
    <div class="content">
      <div>{{comment.content}}</div>
    </div>
    <div class="foot space-between">
      <div class="rate">
        <van-rate v-model="comment.score" allow-half color="#f44" void-icon="star"
                  void-color="#eee"/>
      </div>
      <div class="icon-info">
        <div class="like">
          <span style="font-size: 16px"><font-awesome-icon style="color: #8b9096" :icon="['far','thumbs-up']"/></span>
          <span>{{comment.like}}</span>
        </div>
        <div class="comment">
          <span style="font-size: 16px"><font-awesome-icon style="color: #8b9096" :icon="['far','comment-alt']"/></span>
          <span>{{comment.commentCount}}</span>
        </div>

      </div>
    </div>
    <hr>

  </div>
</template>

<script>
  import { Icon, Rate } from 'vant'

  export default {
    name: 'Comment',
    components: {
      [Icon.name]: Icon,
      [Rate.name]: Rate,
    },
    props: {
      comment: Object
    },
  }
</script>

<style scoped lang="scss">
  span {
    margin-left: 5px;
    vertical-align: middle;
    font-size: 14px;
    color: #8b9096;
  }

  .main {
    margin: 10px 0 0;
    padding: 0 10px;
  }


  .head {
    display: flex;

    .user-avatar {
      flex: 0 0 40px;
      width: 40px;

      img {
        width: 40px;
        border-radius: 30px;
      }
    }

    .head-main {
      display: flex;
      flex: 1;
      align-items: center;
      justify-content: space-between;
      margin-left: 5px;
    }
  }

  .content {
    padding-top: 5px;
  }

  .foot {
    /*line-height: 20px;*/
    padding-top: 6px;

    .icon-info {
      display: flex;
      align-items: start;

      .comment, .like {
        margin-left: 10px;
      }
    }
  }

  .space-between {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }
</style>
