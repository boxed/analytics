// My super simple analytics. I just store referrer, user agent and page counts. The code is at https://github.com/boxed/analytics
function domain_part(s) {
    return s.split('/', 3).join('/');
}

var referrer = null;
if (domain_part(document.referrer) !== domain_part(document.location.href)) {
    referrer = document.referrer;
}

function report_page_load() {
    var data = new FormData();
    data.append('url', document.location);
    data.append('referrer', referrer)

    var request = new XMLHttpRequest();
    request.open('POST', 'https://analytics.kodare.net/report/', true);
    request.send(data);
}

function setup_claps() {
    var claps_count = document.getElementById('claps_count');
    if (claps_count) {
        var claps_request = new XMLHttpRequest();
        var claps_data = new URLSearchParams();
        claps_data.append('url', document.location);
        claps_request.open('GET', 'https://analytics.kodare.net/claps/?' + claps_data.toString(), true);
        claps_request.onload = function () {
            if (claps_request.responseText !== "0") {
                claps_count.innerText = claps_request.responseText + ' claps';
            }
        };
        claps_request.send();
    }
}

report_page_load()
setup_claps()
