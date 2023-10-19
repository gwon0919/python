
function abc() {
    // 입력값을 가져옵니다.
    const su = parseInt(document.getElementById("suInput").value);
    
    // 결과 이미지 엘리먼트를 가져옵니다.
    const resultImg = document.getElementById("resultImg");
    
    // 이미지 파일의 경로를 설정합니다.
    let imagePath;
    if (su % 2 === 0) {
        // 짝수인 경우
        imagePath = "/static/images/sul.jpg";  // 짝수 이미지 파일 경로
    } else {
        // 홀수인 경우
        imagePath = "/static/images/sohee.jpg";  // 홀수 이미지 파일 경로
    }
    
    // 이미지를 표시합니다.
    resultImg.src = imagePath;
    resultImg.style.display = "block";
}