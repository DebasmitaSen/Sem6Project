let line = document.querySelector(".line"),
    loadingprogress = document.querySelector(".loading"),
    progressvalue = document.querySelector(".loadingvalue");

let progressStartvalue = 0,
    progressEndvalue = 100,
    speed = 500;

let progress = setInterval(() => {
    progressStartvalue++

    progressvalue.textContent = `${progressStartvalue}%`
    line.style.width = `${progressStartvalue}%`
    
    if (progressStartvalue == progressEndvalue) {
        clearInterval(progress);
    }
}, speed);