const formFields = document.querySelectorAll(".form-input-container");
const baseSideNav = document.querySelector(".base-sidenav");
const container = document.querySelector(".container");
const contentContainer = document.querySelector(".content-container");
const contentForms = document.querySelectorAll(".content-form");

if (contentForms) {
  contentForms.forEach(contentForm => {
    contentForm.addEventListener("click", e => {
      form = contentForm.lastElementChild;
      cancelBtn = contentForm.querySelector("#content-form-cancel-btn");
        form.classList.remove("hide");
        form.style.width = 'auto';
      contentForm.firstElementChild.classList.add("hide");
      if (e.target.id == "content-form-cancel-btn") {
        form.classList.add("hide");
        contentForm.firstElementChild.classList.remove("hide");
      }
    });
  });
}

function getContentPageWidth(baseSideNav, container) {
  const containerWidth = container.getBoundingClientRect().width;
  const baseSideNavWidth = baseSideNav.getBoundingClientRect().width;
  remainingWidth = containerWidth - baseSideNavWidth;
  contentContainer.style.width = `${remainingWidth}px`;
  console.log(remainingWidth);
}

window.addEventListener("load", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
});

window.addEventListener("resize", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
});

formFields.forEach(formField => {
  formField.addEventListener("keyup", e => {
    const requriedFieldSymbol = formField.querySelector(".form-required-field");
    const formInput = formField.lastElementChild;
    console.log(formInput);
    if (requriedFieldSymbol) {
      if (formInput.value) {
        console.log(requriedFieldSymbol);
        requriedFieldSymbol.classList.add("hide");
      } else {
        requriedFieldSymbol.classList.remove("hide");
      }
    }
  });
});
