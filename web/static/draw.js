cvs=$('#drawing');
ctx=cvs[0].getContext('2d');
ctx.fillStyle="#F0FFF0";
ctx.fillRect(0, 0, cvs[0].width, cvs[0].height);
ctx.lineWidth=20;

var nowx=0;
var nowy=0;
var active=false;
var points=[];
var jsonstr="";


cvs.mousedown(
  function(e){
    nowx=e.pageX-this.offsetLeft;
    nowy=e.pageY-this.offsetTop;
    ctx.moveTo(nowx, nowy);
    register();
    active=true;
  }  
);

cvs.mousemove(
    function(e){
        if(active){
            var getx=e.pageX-this.offsetLeft;
            var gety=e.pageY-this.offsetTop;
            drawline(getx, gety);
            nowx=getx;
            nowy=gety;
            register();
        }   
    }  
  );

 cvs.mouseup(
    function(e){
        active=false;
        $("#data_json").val(JSON.stringify(points));
      } 
 )

function drawline(x,y){
        ctx.lineTo(x,y);
        ctx.stroke();
}

function register(){
    nowxy={x:nowx, y:nowy};
    points.push(nowxy);
}

