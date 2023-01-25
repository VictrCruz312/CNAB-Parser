document.getElementById("store_select").addEventListener("change", function () {
  const selectedStore = this.value;

  if (selectedStore === "Todas") {
    window.location.href = "/app/upload";
  } else {
    window.location.href = "/app/upload?store=" + selectedStore;
  }
});
