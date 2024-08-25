
import Cookies from "js-cookie";
export default {
    mounted() {
        this.SetTheme()
    },
    methods: {
        Theme1() {
            // Проверка наличия элементов
            var head = document.querySelector(".menu");
            if (head) {
                head.classList.remove("bg-dark");
            }

            var navB = document.querySelector(".navbar");
            if (navB) {
                navB.classList.remove("bg-dark");
                navB.classList.add("bg-primary");
            }

            var butt = document.querySelectorAll(".btn-secondary");
            butt.forEach((element) => {
                if (!element.classList.contains("btnClose")) {
                    element.classList.remove("btn-secondary");
                    element.classList.add("btn-primary");
                }
            });

            var modalHead = document.querySelector(".formHeader");
            if (modalHead) {
                modalHead.classList.remove("bg-dark");
            }

            var modalFooter = document.querySelector(".formFooter");
            if (modalFooter) {
                modalFooter.classList.remove("bg-dark");
            }

            var headerText = document.querySelector(".headerText");
            if (headerText) {
                headerText.style.color = "black";
            }

            var btnClose = document.querySelector(".btn-close");
            if (btnClose) {
                btnClose.style.background = "#6c757d";
            }

            var footerColor = document.querySelector("footer");
            if (footerColor) {
                footerColor.classList.remove("bg-dark");
            }

            var footerText = document.querySelectorAll("footer p");
            footerText.forEach((element) => {
                element.style.color = "black";
            });

            var footerLink = document.querySelectorAll("footer a");
            footerLink.forEach((element) => {
                element.style.color = "black";
            });

            var categoryContainer = document.querySelector(".category-container");
            if (categoryContainer) {
                categoryContainer.style.background = "#0d6efd";
            }
            
            var icons = document.querySelectorAll(".icon");
            icons.forEach((element) => {
                element.style.color = "#0d6efd";
            });
            var categoryCounts = document.querySelectorAll('.category-count')
            categoryCounts.forEach((element) => {
                element.style.backgroundColor = '#cadfff'
                element.style.color = '#000'
            })
        },
        Theme2() {

            var head = document.querySelector(".menu");
            if (head) {
                head.classList.add("bg-dark");
            }

            var navB = document.querySelector(".navbar");
            if (navB) {
                navB.classList.add("bg-dark");
                navB.classList.remove("bg-primary");
            }

            var butt = document.querySelectorAll(".btn-primary");
            butt.forEach((element) => {
                element.classList.add("btn-secondary");
                element.classList.remove("btn-primary");
            });

            var modalHead = document.querySelector(".formHeader");
            if (modalHead) {
                modalHead.style.background = "black";
            }

            var modalFooter = document.querySelector(".formFooter");
            if (modalFooter) {
                modalFooter.classList.add("bg-dark");
            }

            var headerText = document.querySelector(".headerText");
            if (headerText) {
                headerText.style.color = "white";
            }

            var btnClose = document.querySelector(".btn-close");
            if (btnClose) {
                btnClose.style.background = "#6c757d";
            }

            var footerColor = document.querySelector("footer");
            if (footerColor) {
                footerColor.classList.add("bg-dark");
            }

            var footerText = document.querySelectorAll("footer p");
            footerText.forEach((element) => {
                element.style.color = "white";
            });

            var footerLink = document.querySelectorAll("footer a");
            footerLink.forEach((element) => {
                element.style.color = "white";
            });
            var categoryContainer = document.querySelector(".category-container");
            if (categoryContainer) {
                categoryContainer.style.background = "#212529";
            }
            var icons = document.querySelectorAll(".icon");
            icons.forEach((element) => {
                element.style.color = "#212529";
            });

            var categoryCounts = document.querySelectorAll('.category-count')
            categoryCounts.forEach((element) => {
                element.style.backgroundColor = '#212529'
                element.style.color = '#fff'
            })
            
        },
        ChangeTheme() {
            var theme = Cookies.get("theme");

            if (theme == "2" || theme === null) {
                Cookies.set("theme", "1");
                this.Theme1();
            } else {
                Cookies.set("theme", "2");
                this.Theme2();
            }
        },
        SetTheme() {
            var theme = Cookies.get("theme");
            if (theme == "2" || theme === null) {
                this.Theme2();
            } else {
                this.Theme1();
            }
        }
    }
}