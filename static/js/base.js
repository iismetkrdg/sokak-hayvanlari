String.prototype.toTitle = function() {
   return this.replace(/(^|\s)\S/g, function(t) { return t.toUpperCase() });
 }
 String.prototype.toDate = function() {
   var value = this.split('T')
   console.log(value)
 }
$(document).ready(function(){
   $("#myModal").modal('show');
});
var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')
if (document.getElementById('myModal')){
   myModal.addEventListener('shown.bs.modal', function () {
      myInput.focus()
    })
    
}








