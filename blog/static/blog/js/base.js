let dropDown = document.getElementsByClassName("drop-down");

myFunction = () => {
    if (dropDown.style.display !== "none") {
        dropDown.style.display = "none";
      } else {
        dropDown.style.display = "block";
      }
}