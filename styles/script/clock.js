/*
 * @Author: your name
 * @Date: 2021-01-30 16:28:43
 * @LastEditTime: 2021-02-04 22:09:30
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \pythontext\styles\script\clock.js
 */


    window.onload = function() {
        CreateHourLines();
        CreateMinLines();
        move();
    }

    function CreateHourLines() {
        /* 绘制钟表的时钟刻度线 */
        var html = "";
        // key1表示x方向上的偏移量，key2表示y方向上的偏移量
        var val, key1, key2;
        for (var i = 0; i < 12; i++) {
            val = i * 30;
            key1 = 88;
            key2 = 0;
            if (val > 180 && val < 360) {
                key1 = 90;
            }
            if (val > 0 && val < 180) {
                key1 = 85
            }

            if (val > 90 && val < 270) {
                key2 = 3;
            }
            if (val < 90 || val > 270) {
                key2 = -3;
            }
            html += "<li style='transform: rotate(" + val + "deg) translate(" + key1 + "px, " + key2 + "px)'></li>";
        }
        $(".hour").html(html);
    }

    function CreateMinLines() {
        /* 绘制钟表的分钟刻度线 */
        var html = "";
        // key1表示x方向上的偏移量，key2表示y方向上的偏移量
        var val, key1, key2;
        for (var i = 0; i < 60; i++) {
            val = i * 6;
            key1 = 90;
            key2 = 0;
            if (val > 90 && val < 270) {
                key2 = 1;
            }
            if (val < 90 || val > 270) {
                key2 = -1;
            }
            html += "<li style='transform: rotate(" + val + "deg) translate(" + key1 + "px, " + key2 + "px)'></li>";
        }
        $(".min").html(html);
    }

    function move() {
        setInterval(function() {
            // 获取当前时刻
            var date = new Date();
            var sec = date.getSeconds();
            var min = date.getMinutes();
            var hour = date.getHours();
            // 计算各指针对应的角度
            var secAngle = sec * 6 - 90; // s*6-90
            var minAngle = min * 6 + sec * 0.1 - 90; // m*6+s*0.1-90
            var hourAngle = hour * 30 + min * 0.5 - 90; // h*30+m*0.5 - 90
            // 转动指针
            $(".p-sec").css("transform", "rotate(" + secAngle + "deg)");
            $(".p-min").css("transform", "rotate(" + minAngle + "deg)");
            $(".p-hour").css("transform", "rotate(" + hourAngle + "deg)");
        }, 1000)
    }
