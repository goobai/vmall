#

#####分类表数据#####
DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS category;
CREATE TABLE `cart`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `sku_id`      bigint(20)  DEFAULT NULL,
    `user_id`     int(11)     DEFAULT NULL,
    `shop_id`     bigint(20)  DEFAULT NULL,
    `count`       int(11)     DEFAULT NULL,
    `checked`     smallint(6) DEFAULT NULL,
    `modify_time` datetime    DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `ix_cart_user_id` (`user_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
CREATE TABLE `category`
(
    `id`        smallint(6) NOT NULL AUTO_INCREMENT,
    `name`      varchar(64) DEFAULT NULL,
    `cid`       smallint(6) DEFAULT NULL,
    `parent_id` smallint(6) DEFAULT NULL,
    `index`     smallint(6) DEFAULT NULL,
    `status`    smallint(6) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 26
  DEFAULT CHARSET = utf8;
insert into category(name, cid, parent_id, `index`, status)
VALUES ('手机数码', 1, 0, 1, 0),
       ('加用电器', 2, 0, 1, 0),
       ('电脑办公', 3, 0, 1, 0),
       ('计身情趣', 4, 0, 1, 0),
       ('美妆护肤', 5, 0, 1, 0),
       ('个人情节', 6, 0, 1, 0),
       ('汽车生活', 7, '0', 1, 0),
       ('维摩超市', 8, '0', 1, 0),
       ('男装', 9, '0', 1, 0),
       ('男鞋', 10, '0', 1, 0),
       ('女装', 11, '0', 1, 0),
       ('女鞋', 12, '0', 1, 0),
       ('母婴童装', 13, '0', 1, 0),
       ('影响图书', 14, '0', 1, 0),
       ('户外运动 ', 15, '0', 1, 0),
       ('内衣配饰', 16, '0', 1, 0),
       ('食品生鲜', 17, '0', 1, 0),
       ('酒水饮料', 18, '0', 1, 0),
       ('家具厨具', 19, '0', 1, 0),
       ('箱包手袋', 20, '0', 1, 0),
       ('钟表珠宝', 21, '0', 1, 0),
       ('玩具乐器', 22, '0', 1, 0),
       ('医疗保健', 23, '0', 1, 0),
       ('宠物生活', 24, '0', 1, 0),
       ('礼品鲜花', 25, '0', 1, 0)
;
insert into shop(name, logo, create_time, modify_time, status)
VALUES ('apple官方旗舰店', '', now(), now(), 0),
       ('华为官方旗舰店', '', now(), now(), 0),
       ('小米官方旗舰店', '', now(), now(), 0),
       ('vivo官方旗舰店', '', now(), now(), 0),
       ('一加官方旗舰店', '', now(), now(), 0),
       ('intel官方旗舰店', '', now(), now(), 0),
       ('amd官方旗舰店', '', now(), now(), 0),
       ('oppo官方旗舰店', '', now(), now(), 0);

insert into product_sku (cid, spu_id, shop_id, name, original_price, price, stock, sales, comments,
                         create_time, modify_time, status)
values (1, 101, 4, '一加 OnePlus 7  骁龙855旗舰性能 4800万超清双摄 8GB+256GB 曜岩灰 全面屏拍照智能游戏手机', 9999, 3999, 2000, 0, '', now(),
        now(), 0),
       (1, 101, 2, '华为 HUAWEI P30 Pro 超感光徕卡四摄10倍混合变焦麒麟980芯片屏内指纹 8GB+256GB极光色全网通版双4G手机', 9999, 5488, 2000, 0, '',
        now(), now(), 0);
insert recommend_product(sku_id, recommend_type, create_time, modify_time, status)
VALUES (1, 1, now(), now(), 0),
       (1, 2, now(), now(), 0),
       (1, 3, now(), now(), 0),
       (2, 1, now(), now(), 0),
       (2, 2, now(), now(), 0),
       (2, 3, now(), now(), 0);

INSERT INTO img (img.url, img.create_time, img.owner_id, img.owner_type)
VALUES ('//m.360buyimg.com/mobilecms/s750x750_jfs/t1/35032/13/9593/102096/5cf0c2ccE77dc890e/abde5c9a60044485.jpg!q80.dpg.webp',
        now(), 3, 3),
       ('//m.360buyimg.com/mobilecms/s750x750_jfs/t1/35032/13/9593/102096/5cf0c2ccE77dc890e/abde5c9a60044485.jpg!q80.dpg.webp',
        now(), 3, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/71005/12/797/89531/5cf0c2c9Ec7c1d689/e4a020636e794015.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/73470/33/825/44204/5cf0c2c9Eb9b4e483/5e59388515cb81cb.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/42848/39/5505/78330/5cf0c2c9E6ea118e8/bc0b114e50896a1b.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/77377/37/790/84433/5cf0c2caE131cf3b1/42084fc54596b4f8.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/48718/34/1244/40378/5cf0c2c9Eb6613d40/25424acf39bc25b1.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/53481/16/1347/89022/5cf0c2cbE6a7e3b1c/8a703893318e114b.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/71152/13/817/156918/5cf0c2cbE2ffd7dbc/b47a22d192dc7522.jpg!q70.dpg.webp',
        now(), 1, 3),
       ('//img20.360buyimg.com/vc/jfs/t1/50719/6/7791/4031633/5d561c2eEc6f0d403/e812ec00e0f29c72.jpg!q70.dpg.webp',
        now(), 1, 4),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/11352/31/13456/324178/5c98c88dE9419c2ca/4be2efca1d9e2b38.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/12083/15/12768/219125/5c98c88dEc05cd5fd/7d41544a66a603d4.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/71005/12/797/89531/5cf0c2c9Ec7c1d689/e4a020636e794015.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/32976/31/7287/127827/5c98c88eE44cc052d/c2c9cf70c60a2771.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/42848/39/5505/78330/5cf0c2c9E6ea118e8/bc0b114e50896a1b.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/24328/36/12407/172691/5c98c88fE3092a5c7/a97b1570083d253e.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/11900/40/13320/116174/5c98c88fEceb3bf93/ca1c903e4a0d7075.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/22846/15/12619/171426/5c98c890E3a126f66/1e5f5f7c2bde2d53.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/11924/21/13365/103494/5c98c890Ee08b17f1/1af644ff101c3512.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/25243/22/12587/126150/5c98c891Ec49e4469/98c2861e676cec62.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//m.360buyimg.com/mobilecms/s843x843_jfs/t1/24662/21/12509/80534/5c98c891Ef0f9ef3e/a5df22f72e51ec29.jpg!q70.dpg.webp',
        now(), 2, 3),
       ('//img20.360buyimg.com/vc/jfs/t1/67327/17/6131/422688/5d43a055E7dcf6f0f/87149d72f5e091a0.jpg!q70.dpg.webp',
        now(), 2, 4),
       ('//img20.360buyimg.com/vc/jfs/t1/76835/34/1814/4930586/5d020cbeEb04bc9c7/09399c32bfabd274.jpg!q70.dpg.webp',
        now(), 2, 4);
