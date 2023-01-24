const form = document.querySelector(".formText");
form.addEventListener("dragover", (e) => {
  e.preventDefault();
  form.classList.add("dragover");
});
form.addEventListener("dragleave", (e) => {
  e.preventDefault();
  form.classList.remove("dragover");
});
form.addEventListener("drop", (e) => {
  e.preventDefault();
  form.classList.remove("dragover");
  const files = e.dataTransfer.files;
  const input = document.querySelector('input[type="file"]');
  input.files = files;
});
