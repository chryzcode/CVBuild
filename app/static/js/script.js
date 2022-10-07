const formFields = document.querySelectorAll(".form-input-container");
const baseSideNav = document.querySelector(".base-sidenav");
const container = document.querySelector(".container");
const contentContainer = document.querySelector(".content-container");
const contentFormContainers = document.querySelectorAll(".content-form-container");
const clickCreateFormInputs = document.querySelectorAll(".click-create-form-input");
const formErrors = document.querySelectorAll(".form-errors");
const allErrorList = document.querySelectorAll(".errorlist");
const linkClickCreateForms = document.querySelectorAll(".link-create-form-btn");

if (clickCreateFormInputs) {
  clickCreateFormInputs.forEach(clickCreateFormInput => {
    const createBtn = clickCreateFormInput.querySelectorAll("span");
    createBtn.forEach(aBtn => {
      aBtn.addEventListener("click", e => {
        const name = e.target.textContent;
        const id = e.target.id;
        let formInput = document.createElement("div");
        formInput.classList.add("form-input-container");
        formInput.innerHTML = `
                 <span><label for="${id}">${name}</label> <span class="faint-text">recommended
                  <span class="material-symbols-outlined remove-field danger icon-pointer">delete
                  </span></span> </span>
                  <p class="form-errors hide">{{ form.${id}.errors }}</p>
                  <input type="text" name="${id}" id="${id}" placeholder=""
                  />
                `;
        aBtn.classList.add("hide");
        clickCreateFormInput.prepend(formInput);
      });
      clickCreateFormInput.addEventListener("click", e => {
        if (e.target.classList.contains("remove-field")) {
          form = e.currentTarget.querySelector("input");
          const formContainer = e.currentTarget.querySelector(".form-input-container");

          formContainer.classList.add("hide");
          aBtn.classList.remove("hide");
        }
      });
    });
  });
}

// clickCreateFormInputs.addEventListener("click", e => {
//   console.log(e.target);
//   if (e.target.classList.contains("remove-field")) {
//     const formInput = e.target.parentElement.parentElement.parentElement;

//     const createFormBtnArray =
//       e.target.parentElement.parentElement.parentElement.parentElement.querySelectorAll(".create-form-btn");
//     createFormBtnArray.append(formInput);
//   formInput.style.display = "none";
//   }
// });

//   clickCreateFormInputs.forEach(clickCreateFormInput => {
//     clickCreateFormInput.addEventListener("click", e => {
//       const id = e.target.id;
//   if (e.target.classList.contains("remove-field")) {
//     form = e.target.parentElement.parentElement.parentElement;
//     formInput = form.querySelector("input");
//     const formFieldName = form.querySelector("label").textContent;
//     const formId = formInput.id;
//     form.classList.add("hide");
//     createFormBtn = document.createElement("span");
//     createFormBtn.id = formId;
//     createFormBtn.innerHTML = `${formFieldName}`;
//     createFormBtn.classList.add("create-form-btn");
//     clickCreateFormInput.prepend(createFormBtn);
//   }
//   console.log(e.target);
//   const element = clickCreateFormInput.querySelector(`#${e.target.id}`);
//   console.log(clickCreateFormInput.querySelector("label"));
//   if (element) {
//     if (e.target == element ) {
//       const name = e.target.textContent;
//       let formInput = document.createElement("div");
//       formInput.classList.add("form-input-container");
//       formInput.innerHTML = `
//          <span><label for="${id}">${name}</label> <span class="faint-text">recommended
//           <span class="material-symbols-outlined remove-field danger icon-pointer">delete
//           </span></span> </span>
//           <p class="form-errors hide">{{ form.${id}.errors }}</p>
//           <input type="text" name="${id}" id="${id}" placeholder=""
//           />
//         `;

//       element.style.display = "none";
//       clickCreateFormInput.prepend(formInput);
//     // }
//   }
//     });
//   });

if (formErrors || allErrorList) {
  formErrors.forEach(formError => {
    setTimeout(() => {
      formError.textContent = "";
      formError.classList.add("hide");
    }, 2000);
  });

  allErrorList.forEach(errorList => {
    setTimeout(() => {
      errorList.textContent = "";
      errorList.classList.add("hide");
    }, 2000);
  });
}
if (contentFormContainers) {
  contentFormContainers.forEach(contentFormContainer => {
    const contentFormDetails = contentFormContainer.querySelector("#content-form-details");
    if (contentFormDetails) {
      contentFormDetails.addEventListener("click", e => {
        if (contentFormContainer == e.currentTarget.parentElement) {
          contentFormContainers.forEach(formContainer => {
            formContainer.classList.add("hide");
          });
        }
        contentFormContainer.classList.remove("hide");
        const linkCreateFormBtn = contentFormContainer.querySelector("#links-form-container");

        linkCreateFormBtn.addEventListener("click", e => {
          const formContainer = e.target.parentElement;
          const allFormInput = linkCreateFormBtn.querySelectorAll("input");

          const clickInput = formContainer.querySelector("input");
          if (clickInput.classList.contains("active")) {
            const formLabel = formContainer.querySelector("label");
            if (e.target == formLabel) {
              clickInput.classList.remove("active");
            }
          } else {
            allFormInput.forEach(allFormBtn => {
              allFormBtn.classList.remove("active");
            });
            clickInput.classList.add("active");
          }
        });
        const form = contentFormDetails.parentElement.querySelector("form");
        const closeBtn = form.querySelector("#content-form-cancel-btn");
        form.classList.remove("hide");
        form.style.width = "auto";
        contentFormDetails.classList.add("hide");
        closeBtn.addEventListener("click", e => {
          form.classList.add("hide");
          contentFormDetails.classList.remove("hide");
          contentFormContainers.forEach(formContainer => {
            formContainer.classList.remove("hide");
          });
        });
      });
    }

    const contentFormTop = contentFormContainer.querySelector("#content-form-top");

    if (contentFormTop) {
      contentFormTop.addEventListener("click", e => {
        if (contentFormContainer == e.currentTarget.parentElement) {
          contentFormContainers.forEach(formContainer => {
            formContainer.classList.add("hide");
          });
          contentFormContainer.classList.remove("hide");
          const icon = contentFormTop.querySelector(".material-symbols-outlined");

          const form = contentFormTop.parentElement.querySelector("form");
          const closeBtn = form.querySelector("#content-form-cancel-btn");

          if (form.classList.contains("hide")) {
            form.classList.remove("hide");
            if (icon) {
              icon.textContent = "expand_less";
            }
          } else {
            form.classList.add("hide");
            contentFormContainers.forEach(formContainer => {
              formContainer.classList.remove("hide");
            });
            if (icon) {
              icon.textContent = "expand_more";
            }
          }
          form.style.width = "auto";

          closeBtn.addEventListener("click", e => {
            form.classList.add("hide");

            if (icon) {
              icon.textContent = "expand_more";
            }

            contentFormContainers.forEach(formContainer => {
              formContainer.classList.remove("hide");
            });
          });
        }
      });
    }
  });
}

function getContentPageWidth(baseSideNav, container) {
  const containerWidth = container.getBoundingClientRect().width;
  const baseSideNavWidth = baseSideNav.getBoundingClientRect().width;
  remainingWidth = containerWidth - baseSideNavWidth;
  contentContainer.style.width = `${remainingWidth}px`;
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
    if (requriedFieldSymbol) {
      if (formInput.value) {
        requriedFieldSymbol.style.display = "none";
      } else {
        requriedFieldSymbol.style.display = "inline-block";
      }
    }
  });
});
