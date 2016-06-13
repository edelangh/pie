
(function() {
    'use strict';
    console.log('PIE script load http');
    var user = 'benjamin';
    setInterval(function() {
        new Promise(function(resolv, reject) {
            var req = new XMLHttpRequest();
            req.open('GET', 'https://pie.cmc.im/tasks/' + user, true);
            req.onreadystatechange = function(aEvt) {
                if (req.readyState == 4) {
                    if (req.status == 200)
                        resolv(req.responseText);
                }
            };
            req.send(null);
        }).then(function(text) {
            var tasks = JSON.parse(text);
            tasks.forEach(function (task, index) {
               if (!task.isFinish) {
                 switch (task.action) {
                     case 'stopYoutube':
                         document.getElementsByTagName('video')[0].pause();
                         break ;
                     case 'open' :
                         window.open(task.data.url, '_blank');
                         break ;
                     case 'nextYoutube':
                         var a = document.getElementsByTagName('video')[0];
                         a.currentTime = a.duration;
                         window.location = document.getElementsByClassName('ytp-upnext-autoplay-icon')[0].href;
                         break ;
                 }
               }
            });
        });
    }, 2000);
    // Your code here...
})();
