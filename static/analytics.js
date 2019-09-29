// My super simple analytics. I just store referrer, user agent and page counts. The code is at https://github.com/boxed/analytics
function domain_part(s) {
    return s.split('/', 3).join('/');
}

var referrer = null;
if (domain_part(document.referrer) !== domain_part(document.location.href)) {
    referrer = document.referrer;
}

// report page load
var data = new FormData();
data.append('url', document.location);
data.append('referrer', referrer)

var request = new XMLHttpRequest();
request.open('POST', 'https://analytics.kodare.net/report/', true);
//request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
request.send(data);
