String.prototype.toTitle = function() {
   return this.replace(/(^|\s)\S/g, function(t) { return t.toUpperCase() });
 }
 String.prototype.toDate = function() {
   var value = this.split('T')
   console.log(value)
 }
$(document).ready(function()
      {
         $.ajax({
            url:'http://127.0.0.1:8000/rest/kulubeler/',
            dataType:'JSON',
            success:function(data)
            {
               for(var i=0;i<data.length;i++)
               {
                  var row=$('<div class="col-sm-4"><div class="card mt-3"><img src="/static/img/'+data[i].img+'" alt="" style="max-width: 414px;max-height: 210px;" class="card-img-top img-fluid"><div class="card-body height-card"><h5 class="card-title">'+data[i].il.toTitle()+'&nbsp;|&nbsp;'+data[i].ilce.toTitle()+'&nbsp;|&nbsp;'+data[i].mahalle.toTitle()+'<p class="card-text">'+data[i].dogcat+' Yuvası</p></h5><p class="card-text ucnokta">'+data[i].aciklama+'</p><div class="row my-date-text mb-5"><p class="card-text text-muted">En son '+data[i].sontarih+'`da beslendi.</p></div><a href="/yuva_details/'+data[i].id+'" class="btn btn-warning width-100 my-button">Detay</a></div></div></div>');
                  $("#kulube").append(row)
               }
               
            }
            
         });
      });
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

