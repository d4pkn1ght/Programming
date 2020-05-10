// MP3
var myPlaylist = new jPlayerPlaylist({
    jPlayer: "#jquery_jplayer_N",
    cssSelectorAncestor: "#jp_container_N"
},
 [
     { title: "Every Breath You Take ", artist: "Music Travel Love", mp3:"images/1.mp3", poster: "images/1.jpg"},
     { title: "Im All About You", artist: "Aaron Carter", mp3:"images/2.mp3 ", poster: "images/2.jpg"},
     { title: "Miss You Like Crazy", artist: "TheMoffatts", mp3:"images/3.mp3", poster: "images/3.jpg"},
     { title: "Best Of Me ", artist: "Daniel Powter", mp3:"images/4.mp3", poster: "images/4.jpg"},
     { title: "Every Day I Love You", artist: "Boyzone", mp3:"images/5.mp3 ", poster: "images/5.jpg"},
     { title: "Your call", artist: "Secondhand Serenade", mp3:"images/6.mp3", poster: "images/6.jpg"},
     { title: "Fall For You ", artist: "Secondhand Serenade", mp3:"images/7.mp3", poster: "images/7.jpg"},
     { title: "Queen Of The Night", artist: "No Name", mp3:"images/8.mp3 ", poster: "images/8.jpg"},
     { title: "Like I Always Do", artist: "Drew", mp3:"images/9.mp3", poster: "images/9.jpg"},
     { title: "Standing still ", artist: "Roman Lob", mp3:"images/10.mp3", poster: "images/10.jpg"},
     { title: "Comethru", artist: "Jeremy Zucker", mp3:"images/11.mp3 ", poster: "images/11.jpg"},
     { title: "Somewhere Only We Know", artist: "Kean", mp3:"images/12.mp3", poster: "images/12.jpg"},

 ],
    {playlistOptions:{enableRemoveControls: true},
    swfPath: "js/",
    supplied: "webmv, ogv, m4v, oga, mp3",
    useStateClassSkin: true,
    autoBlur: false,
    smoothPlayBar: true,
    keyEnabled: true,
    audioFullScreen: true
});


//past
//var latest=[
       // { title: "Dont Give Up On Me ", artist: "Andy Grammer", mp3:"images/13.mp3", poster: "images/13.jpg"},
    //  { title: "Girl Of My Dreams", artist: "The Moffatts", mp3:"images/14.mp3 ", poster: "images/14.jpg"},
    //  { title: "Amen For Women", artist: "Endless Summer", mp3:"images/15.mp3", poster: "images/15.jpg"} 
//];

//now
//var popular=[
     // { title: "Dont Give Up On Me ", artist: "Andy Grammer", mp3:"images/13.mp3", poster: "images/13.jpg"},
    //  { title: "Girl Of My Dreams", artist: "The Moffatts", mp3:"images/14.mp3 ", poster: "images/14.jpg"},
    //  { title: "Amen For Women", artist: "Endless Summer", mp3:"images/15.mp3", poster: "images/15.jpg"} 
//];

//future
//var rank=[
        // { title: "Dont Give Up On Me ", artist: "Andy Grammer", mp3:"images/13.mp3", poster: "images/13.jpg"},
    //  { title: "Girl Of My Dreams", artist: "The Moffatts", mp3:"images/14.mp3 ", poster: "images/14.jpg"},
    //  { title: "Amen For Women", artist: "Endless Summer", mp3:"images/15.mp3", poster: "images/15.jpg"} 
//];

// oline song/dream/
// var main =[
    // { title: "Dont Give Up On Me ", artist: "Andy Grammer", mp3:"images/13.mp3", poster: "images/13.jpg"},
    //  { title: "Girl Of My Dreams", artist: "The Moffatts", mp3:"images/14.mp3 ", poster: "images/14.jpg"},
    //  { title: "Amen For Women", artist: "Endless Summer", mp3:"images/15.mp3", poster: "images/15.jpg"} 
//    ];
// var spirit =[
    // { title: "Dont Give Up On Me ", artist: "Andy Grammer", mp3:"images/13.mp3", poster: "images/13.jpg"},
    //  { title: "Girl Of My Dreams", artist: "The Moffatts", mp3:"images/14.mp3 ", poster: "images/14.jpg"},
    //  { title: "Amen For Women", artist: "Endless Summer", mp3:"images/15.mp3", poster: "images/15.jpg"} 
//    ];
// var magic =[
    // { title: "Dont Give Up On Me ", artist: "Andy Grammer", mp3:"images/13.mp3", poster: "images/13.jpg"},
    //  { title: "Girl Of My Dreams", artist: "The Moffatts", mp3:"images/14.mp3 ", poster: "images/14.jpg"},
    //  { title: "Amen For Women", artist: "Endless Summer", mp3:"images/15.mp3", poster: "images/15.jpg"} 
//    ];



$("#latest li").find("a.playIcon").click(function() {
    var k=$(this).parent("li").index();
    myPlaylist.add({ 
        title:latest[k].title, artist:latest[k].artist,
        //free:true,
        mp3:latest[k].mp3,
        //oga:"",
        poster:latest[k].poster
    });
    myPlaylist.play(-1);
});

$("#popular li").find("a.playIcon").click(function() {
    var k=$(this).parent("li").index();
    myPlaylist.add({ 
        title:popular[k].title, artist:popular[k].artist,
        //free:true,
        mp3:popular[k].mp3,
        //oga:"",
        poster:popular[k].poster
    });
    myPlaylist.play(-1);
});

$("#rank li").find("a.playIcon").click(function() {
    var k=$(this).parent("li").index();
    myPlaylist.add({ 
        title:rank[k].title, artist:rank[k].artist,
        //free:true,
        mp3:rank[k].mp3,
        //oga:"",
        poster:rank[k].poster
    });
    myPlaylist.play(-1);
});

$("#main li").find("a.playIcon").click(function () {
var k = $(this).parent("li").index();
myPlaylist.add({
    title: main[k].title, artist: main[k].artist,
    //free:true,
    mp3: main[k].mp3,
    //oga:"",
    poster: main[k].poster
});
myPlaylist.play(-1);
});

$("#spirit li").find("a.playIcon").click(function () {
var k = $(this).parent("li").index();
myPlaylist.add({
    title: spirit[k].title,
    artist: spirit[k].artist,
    //free:true,
    mp3: spirit[k].mp3,
    //oga:"",
    poster: spirit[k].poster
});
myPlaylist.play(-1);
});
$("#magic li").find("a.playIcon").click(function () {
var m = $(this).parent("li").index();
myPlaylist.add({
    title: magic[m].title,
    artist: magic[m].artist,
    //free:true,
    mp3: magic[m].mp3,
    //oga:"",
    poster: magic[m].poster
});
myPlaylist.play(-1);
});
//Playlist


//remove
$("#playlist-remove").click(function() {
    myPlaylist.remove();		
});

$("#listRemove").click(function() {
    myPlaylist.remove();
});

// next-prev

$("#playlist-next").click(function() {
    myPlaylist.next();
});
$("#playlist-previous").click(function() {
    myPlaylist.previous();
});

// play
$("#playlist-play").click(function() {
    myPlaylist.play();
});

$("#playlist-play--2").click(function() {
    myPlaylist.play(-2);
});
$("#playlist-play--1").click(function() {
    myPlaylist.play(-1);
});
$("#playlist-play-0").click(function() {
    myPlaylist.play(0);
});
$("#playlist-play-1").click(function() {
    myPlaylist.play(1);
});
$("#playlist-play-2").click(function() {
    myPlaylist.play(2);
});

// pause

$("#playlist-pause").click(function() {
    myPlaylist.pause();
});



//autoplay

$("#playlist-option-autoPlay-true").click(function() {
    myPlaylist.option("autoPlay", true);
});
$("#playlist-option-autoPlay-false").click(function() {
    myPlaylist.option("autoPlay", false);
});




//scroll------------------------------------------------------------------------------------------------
var $bar=$(".bar");
var $scrollBar=$(".scrollBar");
var $maxH = $scrollBar.innerHeight() - $bar.outerHeight();
var $ul=$(".jp-playlist ul");
var $li=$(".jp-playlist ul li");
var disY=0; 
var iScale=0;
var iSpeed = 0;

$ul.height(1000);		

$bar.mousedown(function (event){
    var event = event || window.event;
    disY = event.clientY - $(this).position().top;                
    $(document).bind("mousemove",function (event){
            var event = event || window.event;
            var iH = event.clientY - disY;                        
            iH <= 0 && (iH = 0);
            iH >= $maxH && (iH = $maxH);
            $bar.css({top : iH + "px"});
            iScale = - iH/$maxH;
            $ul.css({top:iScale*($ul.height()-$(".jp-playlist-box").height())+"px"});	
            return false;
    });                
    $(document).bind("mouseup",function (){		
            $(document).unbind("mousemove");
            $(document).unbind("mouseup");
    });
    return false;
});

 //playlist-box
$(".jp-playlist-box").mouseover(function(){
        //é¼ æ ‡æ»è½®
        addHandler(this, "mousewheel", mouseWheel);//IE
        addHandler(this, "DOMMouseScroll", mouseWheel);
        return false;			
});

 function addHandler(element, type, handler){
        return element.addEventListener ? element.addEventListener(type, handler, false) :
        element.attachEvent("on" + type, handler, false)
}
 //mousrwheel
function mouseWheel(event){
    var event = event || window.event;
    if(event.wheelDelta) {//IE
            iSpeed = event.wheelDelta > 0 ? -3 : 3;
    }else if(event.detail) {//
            iSpeed = event.detail < 0 ? -3 : 3;
    }
    move();
    
     
    if (event.preventDefault) {  
        event.preventDefault();  
    } 	
} ;
//move
function move(){
    var iH=$bar.position().top;
    iH=iH+iSpeed;
    iH <= 0 && (iH = 0);
    iH >= $maxH && (iH = $maxH);
    $bar.css({top:iH+"px"});
    iScale = - iH/$maxH;
    $ul.css({top:iScale*($ul.height()-$(".jp-playlist-box").height())+"px"});
    return false;
};





var fold=true;


$(".jp-video").animate({left:0},"slow",function(){
    slideOut($(this));		
}).delay(2000).animate({left:"-480px"},350,function(){
    slideIn($(this));	
});


$("#btnfold").mouseover(function(){
    if(fold){
        $(".jp-video").animate({left:"-480px"},350,function(){	
            slideIn($(this));
        });	
    }else{
        $(".jp-video").animate({left:0},350,function(){
            slideOut($(this));
        });	
    }
});

function slideOut(obj){
    $("#btnfold").attr({"title":"slideOut"});
    obj.find("span").css({"transform":"rotate(180deg)"});
    obj.find("span").css({"MozTransform":"rotate(180deg) translateX(2px)"});
    obj.find("span").css({"WebkitTransform":"rotate(180deg)"});
    fold=true;		
};
//Slidein
function slideIn(obj){
    $("#btnfold").attr({"title":"slideIn"});	
    obj.find("span").css({"transform":"rotate(0deg)"});
    obj.find("span").css({"MozTransform":"rotate(0deg) translateX(-2px)"});
    obj.find("span").css({"WebkitTransform":"rotate(0deg)"});
    fold=false;	
};


var iOpen=false;
$("#listClose").click(function(){
    if(iOpen){
        $(".jp-playlist-box").animate({height:0},100);
        $("#btnfold").css({top:"5px"});
        $("#listRemove").css({display:"none"});
        $(".scrollBar").css({display:"none"});
        $(".jp-video").animate({height:"94px",bottom:"20px"},100);
        iOpen=false;
    }else{
        $(".jp-playlist-box").animate({height:"80px"},100);
        $("#btnfold").css({top:"52px"});
        $("#listRemove").css({display:"block"});
        $(".scrollBar").css({display:"block"});
        $(".jp-video").animate({height:"175px",bottom:"20px"},100);
        iOpen=true;
    }
});











