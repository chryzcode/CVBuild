const toogle = document.getElementById("toogle");
const navLinks = document.getElementById("nav-links");
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
const mediumMobileMediaQuery = window.matchMedia("(max-width: 650px)");
const smallMobileMediaQuery = window.matchMedia("(max-width: 450px)");
const inputTextLinkForms = document.querySelectorAll(".input-text-link-form");
const sideNavContents = document.querySelectorAll(".side-nav-content");
const navPageContents = document.querySelectorAll(".nav-page-content");
const addContentBtn = document.querySelector("#add-content-btn");
const feedbacks = document.querySelectorAll(".feedback-container");
const viewMoreFeedbackBtn = document.querySelector("#view-more-feedback-btn");
const addContentModal = document.querySelector("#add-content-modal");
const allModelContents = document.querySelectorAll(".add-modal-content");
const formErrors = document.querySelectorAll(".form-errors");
const createResumeSeg = document.querySelector("#download-resume-seg");

if (mediumMobileMediaQuery.matches) {
  const logos = document.querySelectorAll(".logo");
  logos.forEach(logo => {
    logo.classList.remove("hide");
  });
  if (createResumeSeg) {
    createResumeSeg.classList.remove("hide");
  }
}

if (downloadPdfNav) {
  if (mobileMediaQuery.matches) {
    const desiredWidth = document.querySelector(".content-form-container").getBoundingClientRect().width;
    downloadPdfNav.style.width = `${desiredWidth}px`;
  } else {
    downloadPdfNav.style.width = `${500}px`;
  }
}

function hideSideNav() {
  if (mediumMobileMediaQuery.matches) {
    if (baseSideNav) {
      baseSideNav.classList.add("hide");
    }
  }
}

function showSideNav() {
  if (mediumMobileMediaQuery.matches) {
    if (baseSideNav) {
      baseSideNav.classList.remove("hide");
    }
  }
}

// if (inputTextLinkForms) {
//   inputTextLinkForms.forEach(inputTextLinkForm => {
//     const inputTextLinkFormLabel = inputTextLinkForm.querySelector("label");
//     const inputTextLinkInput = inputTextLinkForm.querySelector("input");
//     inputTextLinkFormLabel.addEventListener("click", e => {
//       const mainInput = e.currentTarget.parentElement.parentElement.querySelector("input");
//       inputTextLinkInput.classList.toggle("hide");
//       mainInput.classList.toggle("hide");
//     });
//   });
// }

if (toogle) {
  toogle.onclick = function () {
    toogle.classList.toggle("active");
    if (navLinks) {
      navLinks.classList.toggle("active");
    }
  };
}

if (addContentBtn) {
  if (document.querySelectorAll(".add-modal-content").length == 0) {
    addContentBtn.classList.add("hide");
  } else {
    addContentBtn.classList.remove("hide");
  }
}

if (allModelContents) {
  // addContentBtn.classList.remove("hide");
  allModelContents.forEach(allModelContent => {
    allModelContent.addEventListener("click", e => {
      e.preventDefault();
      if (document.querySelector(`#${allModelContent.id}-content`)) {
        const content = document.querySelector(`#${allModelContent.id}-content`);
        content.classList.remove("hide");
      }
    });
  });
}
if (feedbacks) {
  if (feedbacks.length > 5) {
    for (var i = 5; i < feedbacks.length; i++) {
      feedbacks[i].style.display = "none";
    }
  } else {
    if (viewMoreFeedbackBtn) {
      viewMoreFeedbackBtn.style.display = "none";
    }
  }

  $(viewMoreFeedbackBtn).click(function () {
    $(".feedback-container:hidden").slice(0, 5).slideDown();
    if ($(".feedback-container:hidden").length == 0) {
      $(viewMoreFeedbackBtn).fadeOut("slow");
    }
  });
}

function copyResumeFeedbackLink() {
  var copyText = document.getElementById("copy-resume-feedback-link");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
}

document.onclick = e => {
  e.preventDefault;
  if (document.querySelector(".resume-pop-up")) {
    if (document.querySelector(".resume-pop-up").classList.contains("hide")) {
      if (e.target.parentElement) {
        if (e.target.parentElement.id == "myresumes-nav") {
          document.querySelector(".resume-pop-up").classList.remove("hide");
          document.querySelector(".content-container").classList.add("overlay");
        }
      }
    } else {
      if (!document.querySelector(".resume-pop-up").classList.contains("hide")) {
        if (e.target !== document.querySelector(".resume-list-container")) {
          document.querySelector(".resume-pop-up").classList.add("hide");
          document.querySelector(".content-container").classList.remove("overlay");
        }
      }
    }
  }
  if (addContentModal) {
    if (addContentModal.classList.contains("hide")) {
      if (e.target.parentElement == addContentBtn) {
        document.querySelector(".content-container").classList.add("overlay");
        document.querySelector(".base-sidenav").classList.add("overlay");
        document.querySelector(".download-pdf-nav").classList.add("overlay");
        addContentModal.classList.remove("hide");
      }
    } else {
      if (e.target.parentElement !== document.querySelector("#add-content-modal")) {
        addContentModal.classList.add("hide");
        document.querySelector(".content-container").classList.remove("overlay");
        document.querySelector(".base-sidenav").classList.remove("overlay");
        document.querySelector(".download-pdf-nav").classList.remove("overlay");
      }
    }
  }
};

if (sideNavContents) {
  sideNavContents.forEach(sideNavContent => {
    sideNavContent.addEventListener("click", e => {
      if (e.currentTarget.id == "check-nav") {
        // baseSideNav.classList.add("hide");
      }
      const theClick = document.querySelector(`#${e.currentTarget.id}-content`);
      if (theClick) {
        navPageContents.forEach(navPageContent => {
          navPageContent.classList.add("hide");
        });
        theClick.classList.remove("hide");
      }
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
          const formContainer = e.target.parentElement.parentElement.parentElement;
          formContainer.classList.add("hide");
          const formContainerId = formContainer.querySelector("input").id;
          const createLinkABtn = clickCreateFormInput.querySelectorAll(".a-btn");
          createLinkABtn.forEach(theBtn => {
            if (theBtn.id == formContainerId) {
              theBtn.classList.remove("hide");
            }
          });
          // aBtn.classList.remove("hide");
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
        if (contentFormContainer.classList.contains("click")) {
          downloadPdfNav.classList.add("hide");
          hideSideNav();
        }

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
          downloadPdfNav.classList.remove("hide");
          showSideNav();
          contentFormDetails.classList.remove("hide");
          contentFormContainers.forEach(formContainer => {
            if (formContainer.classList.contains("container-active")) {
              formContainer.classList.remove("hide");
            }
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
          if (contentFormContainer.classList.contains("click")) {
            downloadPdfNav.classList.add("hide");
            hideSideNav();
          }
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
                    downloadPdfNav.classList.add("hide");
                    hideSideNav();
                    myClickFormContainer.querySelector(".form-display-content-container").classList.add("hide");
                    form.classList.remove("hide");

                    document.querySelector("#add-content-btn").classList.add("hide");
                    const formId = content.id;
                    form.action = "update-" + form.name + "/" + formId + "/";
                    const deleteBtn = form.querySelector("#content-form-delete-btn");
                    deleteBtn.classList.add("a-tag-btn");
                    deleteBtn.parentElement.classList.remove("hide");
                    deleteBtn.classList.remove("hide");
                    deleteBtn.href = "delete-" + form.name + "/" + formId;
                    const formInputContainers = form.querySelectorAll(".form-input-container");
                    if (formInputContainers) {
                      const submitBtn = form.querySelector('button[type="submit"]');

                      formInputContainers.forEach(formInputContainer => {
                        const formInput = formInputContainer.lastElementChild;
                        if (formInput.parentElement.querySelector(".form-required-field")) {
                          formInput.parentElement.querySelector(".form-required-field").classList.add("hide");

                          //   if (!formInput.value) {
                          //     submitBtn.classList.add("disable");
                          //   }
                          // }
                          // submitBtn.classList.add("disable");
                          // form.addEventListener("keyup", e => {
                          //   if (formInput.parentElement.querySelector(".form-required-field")) {
                          //     if (!formInput.value) {
                          //       submitBtn.classList.add("disable");
                          //     } else {
                          //       submitBtn.classList.remove("disable");
                          //     }
                          //   }
                          // });
                          // if (formInput.parentElement.querySelector(".form-required-field")) {
                          //   if (!formInput.value) {
                          //     submitBtn.classList.add("disable");
                          //   }
                        }

                        formInput.addEventListener("change", e => {
                          const selectInput = e.currentTarget.tagName;
                          if (selectInput == "SELECT");
                          {
                            required = form.querySelector(".form-required-field");
                            // if (required.classList.contains("hide")) {
                            //   submitBtn.classList.remove("disable");
                            // }
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
              downloadPdfNav.classList.remove("hide");
              showSideNav();
              if (contentFormContainer.querySelector(".form-display-content-container")) {
                contentFormContainer.querySelector(".form-display-content-container").classList.remove("hide");
              }
              form.id = "";
              form.action = "skill/";
              form.reset();
              document.querySelector("#add-content-btn").classList.remove("hide");

              if (requriedFieldSymbol) {
                requriedFieldSymbol.classList.remove("hide");
              }
              form.classList.add("hide");
              contentFormContainers.forEach(formContainer => {
                if (formContainer.classList.contains("container-active")) {
                  formContainer.classList.remove("hide");
                }
                icon.textContent = "expand_less";

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
              downloadPdfNav.classList.add("hide");
              hideSideNav();
              document.querySelector("#add-content-btn").classList.add("hide");
              contentFormContainer.classList.remove("hide");
              contentFormContainer.querySelector(".form-display-content-container").classList.add("hide");
              contentFormContainer.querySelector("form").classList.remove("hide");

              const closeBtn = contentFormContainer.querySelector("#content-form-cancel-btn");
              closeBtn.addEventListener("click", e => {
                downloadPdfNav.classList.remove("hide");
                showSideNav();
                const requriedFieldSymbol = contentFormContainer.querySelector(".form-required-field");
                document.querySelector("#add-content-btn").classList.remove("hide");
                if (requriedFieldSymbol) {
                  requriedFieldSymbol.classList.remove("hide");
                }
                contentFormTop.classList.remove("hide");
                contentFormContainer.querySelector(".form-display-content-container").classList.remove("hide");
                contentFormContainer.querySelector("form").classList.add("hide");
                icon.textContent = "expand_less";
                contentFormContainers.forEach(formContainer => {
                  if (formContainer.classList.contains("container-active")) {
                    formContainer.classList.remove("hide");
                  }
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
  if (!mediumMobileMediaQuery.matches) {
    {
      const pageWidth = page.getBoundingClientRect().width;
      const baseSideNavWidth = baseSideNav.getBoundingClientRect().width;
      remainingWidth = pageWidth - baseSideNavWidth;
      contentContainer.style.width = `${remainingWidth}px`;
    }
  }
}

function getBaseSideNavHeight(baseSideNav) {
  if (!mediumMobileMediaQuery.matches) {
    const bodyHeight = document.querySelector("body").getBoundingClientRect().height;
    baseSideNav.style.height = `${bodyHeight - 30}px`;
  }
}

window.addEventListener("resize", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
  if (baseSideNav) {
    getBaseSideNavHeight(baseSideNav);
  }

  if (downloadPdfNav) {
    const desiredWidth = document.querySelector(".content-form-container").getBoundingClientRect().width;
    downloadPdfNav.style.width = `${desiredWidth}px`;
    // if (mediumMobileMediaQuery.matches) {
    //   const desiredWidth = document.querySelector(".content-form-container").getBoundingClientRect().width;
    //   // downloadPdfNav.style.width = `${desiredWidth}px`;
    //   downloadPdfNav.style.width = "100%";
    // } else {
    //   downloadPdfNav.style.width = `${500}px`;
    // }
  }

  if (errorTopModal) {
    const allErrorLists = errorTopModal.querySelectorAll("ul");

    allErrorLists.forEach(allErrorList => {
      let error = allErrorList.querySelector(".errorlist");

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

window.addEventListener("load", () => {
  if (baseSideNav && container) {
    getContentPageWidth(baseSideNav, container);
  }
  if (baseSideNav) {
    getBaseSideNavHeight(baseSideNav);
  }

  if (downloadPdfNav) {
    if (mobileMediaQuery.matches) {
      const desiredWidth = document.querySelector(".content-form-container").getBoundingClientRect().width;
      downloadPdfNav.style.width = `${desiredWidth}px`;
    } else {
      downloadPdfNav.style.width = `${500}px`;
    }
  }
});

if (forms) {
  forms.forEach(form => {
    form.querySelectorAll('input[type="checkbox"]').forEach(checkBox => {
      checkBox.previousElementSibling.style.fontSize = `${16}px`;
      checkBox.previousElementSibling.style.color = `#200e32`;
    });

    const startDateInput = form.querySelector(".start-date-input");
    const endDateInput = form.querySelector(".end-date-input");

    form.addEventListener("mouseover", e => {
      const submitBtn = form.querySelector('button[type="submit"]');
      if (startDateInput) {
        if (!startDateInput.value) {
          if (endDateInput) {
            if (endDateInput.value) {
              endDateInput.value = "";

              endDateInput.previousElementSibling.previousElementSibling.textContent = "Start Date is Empty";
              endDateInput.previousElementSibling.style.top = `${50}%`;

              setTimeout(() => {
                endDateInput.previousElementSibling.previousElementSibling.classList.add("hide");
                endDateInput.previousElementSibling.style.top = `${40}%`;
              }, 5000);
            }
          }
        }
      }
      if (startDateInput && endDateInput) {
        if (startDateInput.value && endDateInput.value) {
          if (new Date(endDateInput.value) < new Date(startDateInput.value)) {
            endDateInput.value = "";
            if (
              endDateInput.previousElementSibling.previousElementSibling &&
              endDateInput.previousElementSibling.previousElementSibling.classList.contains("form-errors")
            ) {
              endDateInput.previousElementSibling.style.top = `${50}%`;
              endDateInput.previousElementSibling.previousElementSibling.textContent = "Invalid Date";

              setTimeout(() => {
                endDateInput.previousElementSibling.previousElementSibling.classList.add("hide");
                endDateInput.previousElementSibling.style.top = `${40}%`;
              }, 5000);
            }
          }
        }
      }

      const currentToggleInput = form.querySelector(".current-toggle-checkbox");
      if (startDateInput) {
        if (!startDateInput.value) {
          currentToggleInput.classList.add("disable");
          currentToggleInput.checked = false;
          endDateInput.classList.remove("disable");
        } else {
          currentToggleInput.classList.remove("disable");
        }
      }

      if (currentToggleInput) {
        if (currentToggleInput.checked == true) {
          endDateInput.value = "";
          endDateInput.classList.add("disable");
        }
        currentToggleInput.addEventListener("change", e => {
          if (currentToggleInput.checked == true) {
            if (endDateInput) {
              endDateInput.value = "";
              endDateInput.classList.add("disable");
            }
          } else {
            if (endDateInput) {
              endDateInput.classList.remove("disable");
            }
          }
        });
      }

      const durationToggleChecks = form.querySelectorAll(".duration-toggle-checkbox");
      if (durationToggleChecks) {
        durationToggleChecks.forEach(durationToggleCheck => {
          durationToggleCheck.previousElementSibling.style.fontSize = `${16}px`;
        });
        $(".duration-toggle-checkbox").click(function () {
          $(".duration-toggle-checkbox").not(this).prop("checked", false);
        });
      }

      const formInputContainers = form.querySelectorAll(".form-input-container");
      if (formInputContainers) {
        formInputContainers.forEach(formInputContainer => {
          const requriedFieldSymbol = formInputContainer.querySelector(".form-required-field");

          const formInput = formInputContainer.lastElementChild;

          if (requriedFieldSymbol) {
            if (formInput.value) {
              requriedFieldSymbol.classList.add("hide");
            } else {
              requriedFieldSymbol.classList.remove("hide");
            }
          }

          form.addEventListener("mouseover", e => {
            if (requriedFieldSymbol) {
              if (!requriedFieldSymbol.classList.contains("hide")) {
                submitBtn.classList.add("disable");
              } else {
                submitBtn.classList.remove("disable");
              }
            }
          });

          formInput.addEventListener("keyup", e => {
            if (requriedFieldSymbol) {
              requriedFieldSymbol.style.fontSize = `${25}px`;
              if (formInput.value) {
                requriedFieldSymbol.classList.add("hide");
              } else {
                requriedFieldSymbol.classList.remove("hide");
                submitBtn.classList.add("disable");
              }
            }
          });

          // const inputTextLinkLabel = form.querySelector(".input-text-link-label");
          // if (inputTextLinkLabel) {
          //   inputTextLinkLabel.addEventListener("click", e => {
          //     inputTextLinkLabel.nextElementSibling.classList.toggle("hide");
          //   });
          // }
        });
      }
    });
  });
}
