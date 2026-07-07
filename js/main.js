(function () {
  var ua = navigator.userAgent || "";
  var isAndroid = /Android/i.test(ua);
  var isIOS = /iPhone|iPad|iPod/i.test(ua);
  var btnAndroid = document.getElementById("btn-android");
  var btnIOS = document.getElementById("btn-ios");
  var hint = document.getElementById("device-hint");

  if (isAndroid && btnAndroid) {
    btnAndroid.classList.add("is-highlighted");
    hint.hidden = false;
    hint.textContent = "يبدو أنك تستخدم أندرويد — اضغط الزر الأخضر للتحميل مباشرة.";
  } else if (isIOS && btnIOS) {
    btnIOS.classList.add("is-highlighted");
    hint.hidden = false;
    hint.textContent = "يبدو أنك تستخدم آيفون — افتح الرابط من Safari ثم اضغط زر التحميل.";
  }
})();
