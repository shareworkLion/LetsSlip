// HEADER
function btnSearchClicked() {
  let searchContents = document.querySelector(".form-control").value;
  console.log(`${searchContents}이 검색되었습니다`);
}

// index.html
// bestAwards.html
// 위의 두 파일 동일하게 적용
// 갤러리 넘기는 버튼 눌렀을 때 갤러리 다음 페이지로 넘어가는 기능
const btnForwardEl = document.querySelector(".btnForward");
const btnNextdEl = document.querySelector(".btnNext");

const mainPaginationEl1 = document.querySelector(".gallery-page-1 img");
const mainPaginationEl2 = document.querySelector(".gallery-page-2 img");
const mainPaginationEl3 = document.querySelector(".gallery-page-3 img");
let mainGalleryPageIndex = 0;

function btnForwardClicked() {
  mainGalleryPageIndex -= 1;

  if (mainGalleryPageIndex == 0) {
    btnForwardEl.style.visibility = "hidden";
    btnNextdEl.style.visibility = "visible";

    mainPaginationEl1.src = "../img/Button/Btn_GalleryPaginationActice.png";
    mainPaginationEl2.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl3.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
  } else if (mainGalleryPageIndex == 2) {
    btnForwardEl.style.visibility = "visible";
    btnNextdEl.style.visibility = "hidden";

    mainPaginationEl1.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl2.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl3.src = "../img/Button/Btn_GalleryPaginationActice.png";
  } else {
    btnForwardEl.style.visibility = "visible";
    btnNextdEl.style.visibility = "visible";

    mainPaginationEl1.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl2.src = "../img/Button/Btn_GalleryPaginationActice.png";
    mainPaginationEl3.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
  }
}
function btnNextClicked() {
  mainGalleryPageIndex += 1;

  if (mainGalleryPageIndex == 0) {
    btnForwardEl.style.visibility = "hidden";
    btnNextdEl.style.visibility = "visible";

    mainPaginationEl1.src = "../img/Button/Btn_GalleryPaginationActice.png";
    mainPaginationEl2.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl3.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
  } else if (mainGalleryPageIndex == 2) {
    btnForwardEl.style.visibility = "visible";
    btnNextdEl.style.visibility = "hidden";

    mainPaginationEl1.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl2.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl3.src = "../img/Button/Btn_GalleryPaginationActice.png";
  } else {
    btnForwardEl.style.visibility = "visible";
    btnNextdEl.style.visibility = "visible";

    mainPaginationEl1.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
    mainPaginationEl2.src = "../img/Button/Btn_GalleryPaginationActice.png";
    mainPaginationEl3.src = "../img/Button/Btn_GalleryPaginationDisabled.png";
  }
}

// mySlip.html

// otherUserSlip.html
// function btnClicked(btnName) {
//   document.querySelector(`#btn${btnName} img`).src = `../img/Button/Button_reverse/Btn_${btnName}_Rev.png`
// }
const btnFollowEl = document.querySelector("#btnFollow img");
function btnFollowClicked() {
  console.log("clicked!!");
  btnFollowEl.src = "../img/Button/Button_reverse/Btn_Follow_Rev.png";
}

const btnScrapEl = document.querySelector("#btnScrap img");
function btnScrapClicked() {
  console.log("clicked!!");
  btnScrapEl.src = "../img/Button/Button_reverse/Btn_Scrap_Rev.png";
}

const btnLikesEl = document.querySelector("#btnLikes img");
function btnCommentsClicked() {
  console.log("clicked!!");
  btnLikesEl.src = "../img/Button/Button_reverse/Btn_Likes_Rev.png";
}

const btnCommentsEl = document.querySelector("#btnComments img");
function btnCommentsCliked() {
  console.log("cliked!!");
  btnCommentsEl.src = "../img/Button/Btn_CommentsSmall.png";
  document.querySelector(".slipComments").style.display = "block";
  document.querySelector(".nestedReply").style.display = "none";
  document.querySelector(".createComments").style.display = "block";
}

const btnNestedCommentsEl = document.querySelector("#btnNestedComments img");
function btnNestedCommentsClicked() {
  console.log("cliked!!");
  document.querySelector(".nestedReply").style.display = "block";
}

// myPage2.html
function btnChangeName() {
  let newUserName = document.getElementById("mypageNewId").value;
  console.log(newUserName);
  document.querySelector(".currentUserName").innerHTML = newUserName;
}

// myPage3.html
let newMBTI = [];
function clickedMBTI(MBTI, placeNum) {
  if (newMBTI[placeNum] == null) {
    newMBTI[placeNum] = MBTI;
    console.log(`.mbti-${MBTI} img`);
    document.querySelector(
      `.mbti-${MBTI} img`
    ).src = `../img/Button/MBTI_RAINBOW/MBTI_${MBTI}_Rainbow.png`;
  }
}
function showNewMBTI() {
  if (newMBTI.length === 4) {
    console.log(newMBTI);
    document.querySelector(".currentMBTI").innerHTML = newMBTI
      .toString()
      .replace(/,/g, "");
    window.location.reload();
  }
}

// myPage4.html
function changePWD() {
  let currentPWD = document.getElementById("mypageCurrentPWD").value;
  console.log(currentPWD);
  let changePWD = document.getElementById("mypageNewPWD").value;
  console.log(changePWD);
  let checkPWD = document.getElementById("mypageCheckPWD").value;
  console.log(checkPWD);

  const reg = new RegExp(
    "^(?=.*[A-Za-z])(?=.*d)(?=.*[@$!%*#?&])[A-Za-zd@$!%*#?&]{8,}$"
  );
  if (!reg.test(changePWD)) {
    console.log("형식에 맞지 않음!");
    document.querySelector(".msg2").style.visibility = "visible";
  }

  if (changePWD !== checkPWD) {
    console.log("wrong pwd");
    document.querySelector(".msg3").style.visibility = "visible";
  }
}
