   let page = 1
   const loading = document.querySelector('.dots-8')
   var cont = true
   async function getKulube() {

      const response = await fetch(`https://agile-basin-70896.herokuapp.com/rest/kulubeler/?page=${page}`)

      const kulubeler = await response.json()
      if (kulubeler['next']==null){
         cont = false
         return kulubeler['results'];
      }else{
         return kulubeler['results'];
      }
      
   }
   async function showKulube() {

      const data = await getKulube();

      for (let i = 0; i < data.length; i++) {
         $('#kulube').append('<div class="col-sm-4 "><div class="card mt-3"><img src="/static/img/'+data[i].img+'" alt="" style="max-width: 414px;max-height: 210px;" class="card-img-top img-fluid"><div class="card-body height-card"><h5 class="card-title">'+data[i].il.toTitle()+'&nbsp;|&nbsp;'+data[i].ilce.toTitle()+'&nbsp;|&nbsp;'+data[i].mahalle.toTitle()+'<p class="card-text">'+data[i].dogcat+' Yuvası</p></h5><p class="card-text ucnokta" style="overflow-y: scroll;">'+data[i].aciklama+'</p><div class="row my-date-text mb-5"><p class="card-text text-muted">En son '+data[i].sontarih+'`da beslendi.</p></div><a href="/yuva_details/'+data[i].id+'" class="btn btn-warning width-100 my-button">Detay</a></div></div></div>')
      }
   }
   function showLoading(){
      loading.classList.add('show');
      setTimeout (()=>{
         loading.classList.remove('show');
         page++;
         showKulube();
      },1000);
   }
   window.addEventListener('scroll',() => {
      if (cont==true){
         const { scrollTop , scrollHeight , clientHeight} = document.documentElement;
         if(scrollTop + clientHeight >= scrollHeight){
            showLoading();
         }
      }
   })
   showKulube();