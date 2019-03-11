$('#drawing').mousedown(
  function(e){
      var getx=e.pageX-this.offsetLeft;
      var gety=e.pageY-this.offsetTop;

      $('#test').html(getx+","+gety);
  }  
);