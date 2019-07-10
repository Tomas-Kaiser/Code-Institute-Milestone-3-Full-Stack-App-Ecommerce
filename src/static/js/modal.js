let selectedModel = $('#modalMsg');
console.log("Modal show up")

if (selectedModel.length != 0) {
   selectedModel.modal('show');

   modelClose = () => {
      selectedModel.modal('hide');
   }

   setTimeout(modelClose, 3000);
}
