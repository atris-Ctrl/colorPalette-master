const copyNotification = document.getElementById('copyNotification');

function Copy(color) {
 var cb = document.getElementById(color);
 cb.value = color;
 copyNotification.style.display = 'block';
 setTimeout(() => {
  copyNotification.style.display = 'none';
  }, 2000); // Hide the notification after 2 seconds

 cb.select();
 document.execCommand('copy');
}

