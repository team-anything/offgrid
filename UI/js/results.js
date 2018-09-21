var resultcards=[].slice.call(document.getElementsByClassName("resultcard"));
var summarycards=document.getElementsByClassName("summarycard");

console.log(summarycards);

resultcards.forEach(function(elem,index){
  resultcardorder=index;
  summarycardorder=(parseInt(index/3)+1)*3;
  resultcards[index].style.order=resultcardorder;
  summarycards[index].style.order=summarycardorder;
});

resultcards.forEach(function(elem, index){
  elem.addEventListener("click", function(){
    if(summarycards[index].classList.contains('is-open')){
      $('.is-open').toggleClass('is-open');
      $('.active').toggleClass('active');
    }
    else {
      $('.is-open').toggleClass('is-open');
      summarycards[index].classList.add('is-open');
      $('.active').toggleClass('active');
      resultcards[index].classList.add('active');
    }
    // console.log(resultcards[index]);
  });
});