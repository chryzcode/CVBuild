const formFields = document.querySelectorAll(".form-input-container");
const forms = document.querySelectorAll("form");
const baseSideNav = document.querySelector(".base-sidenav");
const container = document.querySelector(".container");
const contentContainer = document.querySelector(".content-container");
const contentFormContainers = document.querySelectorAll(".content-form-container");
const clickCreateFormInputs = document.querySelectorAll(".click-create-form-input");
const errors = document.querySelectorAll(".errors");
const allErrorList = document.querySelectorAll(".errorlist");
const linkClickCreateForms = document.querySelectorAll(".link-create-form-btn");
const downloadPdfNav = document.querySelector(".download-pdf-nav");
const errorTopModal = document.querySelector(".error-top-modal");
const mobileMediaQuery = window.matchMedia("(max-width: 950px)");
const inputTextLinkForms = document.querySelectorAll(".input-text-link-form");

if (inputTextLinkForms) {
  inputTextLinkForms.forEach(inputTextLinkForm => {
    const inputTextLinkFormLabel = inputTextLinkForm.querySelector("label");
    const inputTextLinkInput = inputTextLinkForm.querySelector("input");
    inputTextLinkFormLabel.addEventListener("click", e => {
      const mainInput = e.currentTarget.parentElement.parentElement.querySelector("input");
      inputTextLinkInput.classList.toggle("hide");
      mainInput.classList.toggle("hide");
    });
  });
}

function search() {
  var input, filter, btns, span, i, txtValue;

  input = document.querySelector("#link-search-bar");
  filter = input.value.toUpperCase();
  allBtnsContainer = document.querySelector(".link-create-form-btn");
  btns = allBtnsContainer.querySelectorAll("span");

  for (i = 0; i < btns.length; i++) {
    span = btns[i];
    txtValue = span.textContent || span.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      btns[i].classList.remove("hide");
    } else {
      btns[i].classList.add("hide");
    }
  }
}

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
          const formContainer = e.currentTarget.querySelector(".form-input-container");
          formContainer.classList.add("hide");
          aBtn.classList.remove("hide");
        }
      });
    });
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
        document.querySelector("#add-content-btn").classList.add("hide");
        contentFormDetails.classList.add("hide");
        closeBtn.addEventListener("click", e => {
          form.classList.add("hide");
          contentFormDetails.classList.remove("hide");
          contentFormContainers.forEach(formContainer => {
            formContainer.classList.remove("hide");
            document.querySelector("#add-content-btn").classList.remove("hide");
          });
        });
      });
    }

    const contentFormTop = contentFormContainer.querySelector("#content-form-top");
    const form = contentFormContainer.querySelector(".content-form");
    if (form) {
      if (contentFormTop) {
        contentFormTop.addEventListener("click", e => {
          const icon = contentFormTop.querySelector("#toggle-icon");
          const myClick = e.currentTarget;
          if (e.currentTarget == myClick) {
            const myClickFormContainer = myClick.parentElement;
            const contentDetail = myClickFormContainer.querySelector(".form-display-content-container");

            if (contentDetail) {
              if (form.classList.contains("hide")) {
                contentDetail.classList.toggle("hide");
                const contents = contentDetail.querySelectorAll(".form-display-content");

                contents.forEach(content => {
                  content.addEventListener("click", e => {
                    myClickFormContainer.querySelector(".form-display-content-container").classList.add("hide");
                    form.classList.remove("hide");
                    document.querySelector("#add-content-btn").classList.add("hide");
                    const formId = e.target.id;
                    form.action = "update-" + form.name + "/" + formId;
                    const deleteBtn = form.querySelector("#content-form-delete-btn");
                    deleteBtn.parentElement.classList.remove("hide");
                    deleteBtn.classList.remove("hide");
                    console.log(form.name);
                    deleteBtn.href = "delete-" + form.name + "/" + formId;
                    const formInputContainers = form.querySelectorAll(".form-input-container");
                    if (formInputContainers) {
                      const submitBtn = form.querySelector('button[type="submit"]');

                      formInputContainers.forEach(formInputContainer => {
                        const formInput = formInputContainer.lastElementChild;
                        if (formInput.parentElement.querySelector(".form-required-field")) {
                          formInput.parentElement.querySelector(".form-required-field").classList.add("hide");
                          if (!formInput.value) {
                            submitBtn.classList.add("disable");
                          }
                        }
                        submitBtn.classList.add("disable");
                        form.addEventListener("keyup", e => {
                          if (formInput.parentElement.querySelector(".form-required-field")) {
                            if (!formInput.value) {
                              submitBtn.classList.add("disable");
                            } else {
                              submitBtn.classList.remove("disable");
                            }
                          }
                        });
                        if (formInput.parentElement.querySelector(".form-required-field")) {
                          if (!formInput.value) {
                            submitBtn.classList.add("disable");
                          }
                        }

                        formInput.addEventListener("change", e => {
                          const selectInput = e.currentTarget.tagName;
                          if (selectInput == "SELECT");
                          {
                            required = form.querySelector(".form-required-field");
                            if (required.classList.contains("hide")) {
                              submitBtn.classList.remove("disable");
                            }
                          }
                        });
                      });
                    }

                    contentFormContainers.forEach(formContainer => {
                      formContainer.classList.add("hide");
                    });

                    contentFormContainer.classList.remove("hide");
                    closeContentForm();
                  });
                });
              }
              if (form.classList.contains("hide")) {
                if (icon.textContent == "expand_less") {
                  icon.textContent = "expand_more";
                } else {
                  icon.textContent = "expand_less";
                }
              }
            } else {
              document.querySelector("#add-content-btn").classList.add("hide");
              icon.textContent = "expand_less";
            }
          }

          function closeContentForm() {
            const closeBtn = form.querySelector("#content-form-cancel-btn");

            form.classList.remove("hide");
            const requriedFieldSymbol = form.querySelector(".form-required-field");

            closeBtn.addEventListener("click", e => {
              form.id = "";
              form.action = "skill/";
              form.reset();
              document.querySelector("#add-content-btn").classList.remove("hide");

              if (requriedFieldSymbol) {
                requriedFieldSymbol.classList.remove("hide");
              }
              form.classList.add("hide");
              contentFormContainers.forEach(formContainer => {
                formContainer.classList.remove("hide");
                icon.textContent = "expand_more";

                if (form.querySelector("select") && form.querySelector("option")) {
                  if (form.querySelector("option").classList.contains("current_value")) {
                    form.querySelector("option").classList.add("hide");
                    form.querySelector("option").innerHTML = "";
                    form.querySelector("option").value = "";
                  }
                }
              });
            });
          }

          contentFormContainers.forEach(formContainer => {
            if (!contentFormContainer.querySelector(".form-display-content-container")) {
              formContainer.classList.add("hide");
            }
          });

          if (!contentFormContainer.querySelector(".form-display-content-container")) {
            contentFormContainer.classList.remove("hide");
            closeContentForm();
          } else {
            const addFormBtn = contentFormContainer.querySelector("#add-display-content-form");

            addFormBtn.addEventListener("click", e => {
              contentFormContainers.forEach(formContainer => {
                formContainer.classList.add("hide");
              });
              document.querySelector("#add-content-btn").classList.add("hide");
              contentFormContainer.classList.remove("hide");
              contentFormContainer.querySelector(".form-display-content-container").classList.add("hide");
              contentFormContainer.querySelector("form").classList.remove("hide");

              const closeBtn = contentFormContainer.querySelector("#content-form-cancel-btn");
              closeBtn.addEventListener("click", e => {
                const requriedFieldSymbol = contentFormContainer.querySelector(".form-required-field");
                document.querySelector("#add-content-btn").classList.remove("hide");
                if (requriedFieldSymbol) {
                  requriedFieldSymbol.classList.remove("hide");
                }
                contentFormTop.classList.remove("hide");
                contentFormContainer.querySelector(".form-display-content-container").classList.add("hide");
                contentFormContainer.querySelector("form").classList.add("hide");
                icon.textContent = "expand_more";
                contentFormContainers.forEach(formContainer => {
                  formContainer.classList.remove("hide");
                });
              });
            });
          }
        });
      }
    }
  });
}

function getContentPageWidth(baseSideNav, page) {
  const pageWidth = page.getBoundingClientRect().width;
  const baseSideNavWidth = baseSideNav.getBoundingClientRect().width;
  remainingWidth = pageWidth - baseSideNavWidth;
  contentContainer.style.width = `${remainingWidth}px`;
}

function getBaseSideNavHeight(baseSideNav) {
  const bodyHeight = document.querySelector("body").getBoundingClientRect().height;
  baseSideNav.style.height = `${bodyHeight}px`;
}

window.addEventListener("load", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
  if (baseSideNav) {
    getBaseSideNavHeight(baseSideNav);
  }

  if (mobileMediaQuery.matches) {
    const desiredWidth = document.querySelector(".content-form-container").getBoundingClientRect().width;
    downloadPdfNav.style.width = `${desiredWidth}px`;
  } else {
    downloadPdfNav.style.width = `${500}px`;
  }

  if (errorTopModal) {
    const allErrorLists = errorTopModal.querySelectorAll("ul");

    allErrorLists.forEach(allErrorList => {
      const error = allErrorList.querySelector(".errorlist");
      if (error) {
        error.classList.remove(".errorlist");
        error.style.listStyle = "revert";
        error.style.textAlign = "left";
      }
    });

    setTimeout(() => {
      errorTopModal.classList.add("hide");
    }, 5000);
  }
});

if (!errorTopModal) {
  if (allErrorList) {
    allErrorList.forEach(error => {
      error.style.textTransform = "capitalize";
      error.style.fontSize = "14px";
      setTimeout(() => {
        error.classList.add("hide");
      }, 5000);
    });
  }
}

window.addEventListener("resize", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
  if (baseSideNav) {
    getBaseSideNavHeight(baseSideNav);
  }

  if (mobileMediaQuery.matches) {
    const desiredWidth = document.querySelector(".content-form-container").getBoundingClientRect().width;
    downloadPdfNav.style.width = `${desiredWidth}px`;
  } else {
    downloadPdfNav.style.width = `${500}px`;
  }
});

if (forms) {
  forms.forEach(form => {
    form.addEventListener("mouseover", e => {
      const submitBtn = form.querySelector('button[type="submit"]');

      const formInputContainers = form.querySelectorAll(".form-input-container");
      if (formInputContainers) {
        formInputContainers.forEach(formInputContainer => {
          const requriedFieldSymbol = formInputContainer.querySelector(".form-required-field");

          const formInput = formInputContainer.lastElementChild;
          const allFormRequiredSymbol = form.querySelectorAll(".form-required-field");

          formInput.addEventListener("keyup", e => {
            if (requriedFieldSymbol) {
              requriedFieldSymbol.style.fontSize = `${25}px`;
              if (formInput.value) {
                requriedFieldSymbol.classList.add("hide");
          
              } else {
                requriedFieldSymbol.classList.remove("hide");
              
              }
            }
          });

          if (requriedFieldSymbol) {
            if (!requriedFieldSymbol.classList.contains("hide")) {
              submitBtn.classList.add("disable");
            } else {
              submitBtn.classList.remove("disable");
            }
          }

          const inputTextLinkLabel = form.querySelector(".input-text-link-label");
          if (inputTextLinkLabel) {
            inputTextLinkLabel.addEventListener("click", e => {
              inputTextLinkLabel.nextElementSibling.classList.toggle("hide");
            });
          }
        });
      }
    });
  });
}
