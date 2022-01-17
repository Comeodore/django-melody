counter = document.querySelector(".counter")
floorpath = document.querySelectorAll(".default-path")
floorpath[0].classList.add("path-hover")
floordata = []

HOST = 'https://melody.pp.ua/'

function Show(last_id,id)
{
    floorpath[last_id-1].classList.remove("path-hover")
    floorpath[id-1].classList.add("path-hover")
}

function FindId(el,floorpath)
{
    for(i = 0;i<floorpath.length;i++)
    {
        if(el === floorpath[i])
        {
            return i
        }
    }
}

function NewCounter(last_id,id)
{
    if(id < 10 && id > 0)
    {
        counter.style.paddingRight = 0
        counter.textContent = "0" + id
        Show(last_id,id)
    }
    if(id < 18 && id >= 10){
        counter.style.paddingRight = '8px'
        counter.textContent = id
        Show(last_id,id)
    }
}

document.getElementById("up").onclick = function ()
{
    id = Number(counter.textContent)
    NewCounter(id,++id)
}

document.getElementById("down").onclick = function ()
{
    id = Number(counter.textContent)
    NewCounter(id,--id)
}

floorpath.forEach(el =>
     el.addEventListener("mouseover", function(){
         id = FindId(el,floorpath)
         NewCounter(Number(counter.textContent),id+1);
         SetCounterToNumFloor()
     })
)

function SetCounterToNumFloor()
{
    document.querySelector(".num-floor").textContent = counter.textContent
}


floorpath.forEach(el =>
     el.addEventListener("click", function(){
        GetDataOnFloor();
        document.querySelector(".choose-flats").classList.add('animate__fadeInDown');
        document.querySelector(".choose-flats-bg").classList.add('open')
     })
)

document.querySelector(".show-flats-btn").onclick = function ()
{
    SetCounterToNumFloor()
    GetDataOnFloor()
    document.querySelector(".choose-flats").classList.add('animate__fadeInDown')
    document.querySelector(".choose-flats-bg").classList.add('open')
}

document.querySelector(".close-but").onclick = function ()
{
    RemoveReserved()
    document.querySelector(".choose-flats").classList.remove('animate__fadeInDown')
    document.querySelector(".choose-flats-bg").classList.remove('open')
}

a_flats = document.querySelectorAll(".item-info-floor")
path_flats = document.querySelectorAll(".flats-path")

function GetDataOnFloor()
{
    span_flats = document.querySelectorAll(".flat-number")
    fetch(HOST + 'api/flats/?floor='+ Number(counter.textContent) + '&format=json')
      .then(
        function(response) {
          response.json().then(function(data) {
              floordata = data
            for (i = 0;i<10;i++)
            {
                span_flats[i].textContent = data[i]['id']
                if(data[i]['reserved'] === true)
                {
                    a_flats[i].classList.add('flat-reserved')
                    path_flats[i].classList.add('path-flat-reserved')
                }
            }
          });
        }
      );
}

function RemoveReserved()
{
    for (i = 0;i<10;i++)
    {
        if(a_flats[i].classList.contains('flat-reserved'))
        {
            a_flats[i].classList.remove('flat-reserved')
        }
        if(path_flats[i].classList.contains('path-flat-reserved'))
        {
            path_flats[i].classList.remove('path-flat-reserved')
        }
    }
}

function AFlatsHover(el)
{
    if(!el.classList.contains('flat-reserved'))
         {
            el.classList.toggle('flats-hover')
            path_flats[FindId(el,a_flats)].classList.toggle('path-hover')
         }
}

a_flats.forEach(el =>
     el.addEventListener("mouseover", function(){
         AFlatsHover(el)
     })
)

a_flats.forEach(el =>
     el.addEventListener("mouseout", function(){
         AFlatsHover(el)
     })
)

function PathFlatsHover(el)
{
    if(!el.classList.contains('path-flat-reserved'))
         {
            el.classList.toggle('path-hover')
            a_flats[FindId(el,path_flats)].classList.toggle('flats-hover')
         }
}

path_flats.forEach(el =>
     el.addEventListener("mouseover", function(){
         PathFlatsHover(el)
     })
)

path_flats.forEach(el =>
     el.addEventListener("mouseout", function(){
         PathFlatsHover(el)
     })
)

function Payment(id)
{
    document.location.href = HOST + 'buy/' + id
}

path_flats.forEach(el =>
     el.addEventListener("click", function(){
         if(!el.classList.contains('path-flat-reserved'))
         {
             Payment(floordata[FindId(el,path_flats)]['id'])
         }
     })
)

a_flats.forEach(el =>
     el.addEventListener("click", function(){
         if(!el.classList.contains('flat-reserved')) {
            Payment(floordata[FindId(el,a_flats)]['id'])
         }
     })
)
