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