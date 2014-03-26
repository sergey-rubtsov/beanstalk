$(function () {
    var settings = {
        showArrows: true

    };
    var pane = $('.scroll-pane')
    pane.jScrollPane(settings);
    var api = pane.data('jsp');
    var block = 1;
    var cloud = 1;

    function addBlock() {

        if (block > 6) {
            block = Math.floor((Math.random() * 5) + 2);
        }

        if (Math.floor((Math.random() * 10)) == 7) {
            cloud = Math.floor((Math.random() * 4) + 1);
            api.getContentPane().append(
                '<div class="beanstalk beanstalk-' + block++ + '"><div class="cloud cloud-' + cloud + '"></div></div>'
            );

        } else {
            api.getContentPane().append(
                '<div class="beanstalk beanstalk-' + block++ + '"></div>'
            );
        }
        api.reinitialise();
    }

    for (var j = 0; j < 200; j++) {
        addBlock();
    }

    var position = 2000;
    api.scrollToY(position);

    var i = 0;

    setInterval(
        function () {
            i++;

            if (i < 500) {
                var tmp = (Math.sin(i) * ((500 - i) / 100));
                position = position + Math.abs(Math.floor(tmp));
                api.scrollToY(position)
            }
        },
        10
    );
});
