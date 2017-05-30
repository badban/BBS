function search() {
    var keyword = $('#search').val();
    var dst = "/search/" + keyword + "/";
    if (keyword != '') {
        window.location = dst;
    } else {
        alert('请输入您要搜索的关键词。')
        return false;
    };
}

$(document).ready(function(){
    $('#search-btn').click(
        function(){
          search();
        }
    );
});

$(function () {
    //修改提示信息显示样式
    $.testRemind.css = {
        padding: "8px 10px",
        borderColor: "#aaa",
        borderRadius: 8,
        boxShadow: "2px 2px 4px rgba(0,0,0,.2)",
        background: "#fff url(chrome-remind.png) no-repeat 10px 12px",
        backgroundColor: "#fff",
        fontSize: 14,
        textIndent: 20
    };

    $('#reg-check').html5Validate(function () {
        alert("验证成功");
        this.submit();
    }, {
        validate: function () {
            var password = $('#password').val();
            var checkPassword = $('#password2').val();
            if (password != checkPassword) {
                $('#password2').testRemind('前后密码不一致');
                return false;
            }
            return true;
        }
    });
});