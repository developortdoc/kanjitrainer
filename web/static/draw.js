ctx=$('#drawing')[0].getContext('2d');
ctx.lineWidth=20;
var nowx=0;
var nowy=0;
var active=false;

$('#drawing').mousedown(
  function(e){
    nowx=e.pageX-this.offsetLeft;
    nowy=e.pageY-this.offsetTop;
    ctx.moveTo(nowx, nowy);
    active=true;
  }  
);

$('#drawing').mousemove(
    function(e){
        if(active){
            var getx=e.pageX-this.offsetLeft;
            var gety=e.pageY-this.offsetTop;
            drawline(getx, gety);
            nowx=getx;
            nowy=gety;
        }   
    }  
  );

 $('#drawing').mouseup(
    function(e){
        active=false;
      } 
 )

  function drawline(x,y){
        ctx.lineTo(x,y);
        ctx.stroke();
  }


