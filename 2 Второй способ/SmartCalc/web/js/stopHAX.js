
function stopHAX(event) {
    event.preventDefault();
    event.stopPropagation();
    alert("Не нужно трогать эти кнопки");
}

window.oncontextmenu = function(event) {
    // block right-click / context-menu
    stopHAX(event);
    return false;
};

window.addEventListener("keydown", function(event) {
    if (event.keyCode == 116) {
        // block F5 (Refresh)
        stopHAX(event);
        return false;

    } else if (event.keyCode == 122) {
        // block F11 (Fullscreen)
        stopHAX(event);
        return false;

    } else if (event.keyCode == 123) {
        // block F12 (DevTools)
        stopHAX(event);
        return false;

    } else if (event.ctrlKey && event.shiftKey && event.keyCode != 0) {
        // block Strg+Shift+I (DevTools)
        stopHAX(event);
        return false;

    }
});
window.addEventListener("resize", function(){
    window.resizeTo(420, 720);
    });