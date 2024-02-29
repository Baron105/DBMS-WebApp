function changeReadMore(eventId) {
    
    const myButton = document.getElementById('read-more-btn-'+eventId);
    const threeDots = document.getElementById('three-dots-'+eventId);
    const fullDesc = document.getElementById('full-desc-'+eventId);
    const eventTiming = document.getElementById('event-timings-'+eventId);

    if (fullDesc.style.display === 'none' || fullDesc.style.display === '') {
        fullDesc.style.display = 'inline';
        threeDots.style.display = 'none';
        myButton.textContent = 'Read Less';
        eventTiming.style.display = 'none';
    } 
    
    else {
        fullDesc.style.display = 'none';
        threeDots.style.display = 'inline';
        myButton.textContent = 'Read More';
        eventTiming.style.display = 'flex';
    }
}

var et = document.querySelector('#my_variable').value

    function toggleDiv1() {
        var div = document.getElementById('div1');
        var div2 = document.getElementById('div2');
        var div3 = document.getElementById('div3');
        div.style.display = 'block';
        div2.style.display = 'none';
        div3.style.display = 'none';
        
    }
    function toggleDiv2() {
        var div = document.getElementById('div2');
        var div1 = document.getElementById('div1');
        var div3 = document.getElementById('div3');
        div.style.display = 'block';
        div1.style.display = 'none';
        div3.style.display = 'none';

    }
    function toggleDiv3() {
        var div = document.getElementById('div3');
        var div1 = document.getElementById('div1');
        var div2 = document.getElementById('div2');
        div.style.display = 'block';
        div1.style.display = 'none';
        div2.style.display = 'none';
    }
    function load(et){
        if(et == 1) {
            toggleDiv2();
        }
        else if(et == 2) {
            toggleDiv3();
        }
        else {
            toggleDiv1();
        }
    }