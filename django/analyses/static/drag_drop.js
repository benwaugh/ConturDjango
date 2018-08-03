function onDrag(event) {
    event.dataTransfer.setData('Text', 'Some content');
}

window.onload = function() {
    document.querySelector("iframe").srcdoc = "<body ondragover='event.preventDefault();'
}