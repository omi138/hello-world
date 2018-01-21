function callarr()
{
    var arr = [];
    for (var i =0;i< 3;i++)
    {
       // var j = i;
        arr.push((function(j){                 //called at run time on the fly
            j = i;
            return j;
        })(i));
    }
    
    return arr;
}


var result = callarr();
console.log(result);

var onecall = function(num){                    //function is called o the fly

return num;
}('hi');

console.log(onecall);
console.log(onecall);