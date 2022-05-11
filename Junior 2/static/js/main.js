const visit_random = () => {

    var urls = new Array();

    urls[0] = "https://c-phrase.com"; //my company!
    urls[1] = "https://getbootstrap.com/docs/5.1/getting-started/introduction/";
    urls[2] = "https://reactjs.org";
    urls[3] = "https://w3.org";
    urls[4] = "https://flask.palletsprojects.com/en/2.1.x/#"

    var random = Math.floor(Math.random() * urls.length);

    window.open(urls[random], '_blank');
};