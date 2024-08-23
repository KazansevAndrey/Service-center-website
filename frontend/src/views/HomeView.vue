<template>
  <div class="home">
    <section>
      <div class="caroudel">
        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel" data-bs-interval="8000">
          <ol class="carousel-indicators">
            <li type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
              aria-current="true" aria-label="Slide 1"></li>
            <li type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2">
            </li>
            <li type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3">
            </li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="../assets/images/slide1.jpg" class="d-block w-100" alt="слайд 1">
              <div class="carousel-caption">
                <h5>У наших мастеров огромный опыт работы</h5>
                <p class="textSlide">
                  Наши мастера опытны в ремонте и обслуживании компьютерной техники для домашних и
                  корпоративных клиентов, гарантируя высокое качество работы.
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="../assets/images/slide2.jpg" class="d-block w-100" alt="слайд 2">
              <div class="carousel-caption">
                <h5>В нашем магазине большой ассортимент аксесуаров</h5>
                <p class="textSlide">
                  В нашем магазине вы найдете широкий ассортимент аксессуаров для телефонов, включая чехлы,
                  пленки, наушники и зарядные устройства. Мы предлагаем лучшие и инновационные решения, следя
                  за последними тенденциями.
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="../assets/images/slide3.jpg" class="d-block w-100" alt="слайд 3">
              <div class="carousel-caption">
                <h5>У нас приемлемые цены</h5>
                <p class="textSlide">
                  В нашем магазине вы найдете передовые продукты по доступным ценам.
                  Мы предлагаем лучшее соотношение цены и качества, чтобы современные устройства были доступны каждому.
                </p>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
          </button>
        </div>
      </div>

      <div class="container">

        <div class="heading">
          <h2 class="headingLeft">СЕРВИСНЫЙ ЦЕНТР <b>SERVICE CENTER</b> - ВЕРНЕМ ВАШУ ТЕХНИКУ К ЖИЗНИ!</h2>
          <img src="../assets/images/master1.webp" class="headingImg" alt="Тут должна быть картинка">
        </div>

        <p class="text">Сервисный центр SERVICE CENTER - это не просто место ремонта техники, это место, где
          мы с любовью и профессионализмом восстанавливаем вашу технику. Мы понимаем,
          насколько важны для вас ваши устройства, поэтому предлагаем качественные услуги
          по ремонту и обслуживанию, чтобы ваши гаджеты работали безупречно и долго. Доверьте
          нам свои технические проблемы, и мы сделаем все возможное, чтобы вернуть вам рабочее
          состояние вашей техники в кратчайшие сроки.
        </p>

        <div class="heading head2">
          <img src="../assets/images/comp.webp" class="headingImg" alt="Тут должна быть картинка">
          <h2 class="headingRight">ХОТИТЕ ОБНОВИТЬ СВОЙ КОМПЬЮТЕР? <b>SERVICE CENTER</b> ПОМОЖЕТ ВАМ!</h2>
        </div>

        <p class="text">Хотите освежить свой компьютер? SERVICE CENTER поможет вам в этом! Наши полки полны широкого
          выбора компонентов и аксессуаров, готовых привнести новую жизнь в ваше устройство. Наши консультанты
          всегда готовы помочь вам выбрать идеальные обновления, подходящие вашим потребностям. Доверьтесь SERVICE
          CENTER и наслаждайтесь улучшенным опытом работы с вашим компьютером!
        </p>

        <div class="heading">
          <h2 class="headingLeft">НУЖЕН ЧЕХОЛ ДЛЯ НОВОГО ТЕЛЕФОНА? ВАМ В <b>SERVICE CENTER</b></h2>
          <img src="../assets/images/iphone.webp" class="headingImg iphoneImg" alt="Тут должна быть картинка">
        </div>

        <p class="text">Вам нужен чехол для своего нового телефона? Обратитесь в SERVICE CENTER! У нас вас ждет
          огромный выбор аксессуаров, включая стильные и надежные чехлы для защиты вашего устройства. Наши
          консультанты всегда готовы помочь вам выбрать идеальный чехол, который подойдет как по функциональности,
          так и по дизайну. Защитите свой телефон с SERVICE CENTER!
        </p>

        <h2 class="HeadingText">СЕРТИФИКАТЫ</h2>
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div id="gallery" class="row"></div>
            </div>
          </div>
        </div>

        <h2 class="HeadingText">Количество отремонтированной техники за прошлый год (в %)</h2>
        <canvas id="repairChart"></canvas>

        <div class="orderCall">
          <!-- Button trigger modal -->
          <button type="button" class="btn btn-primary " data-bs-toggle="modal" data-bs-target="#exampleModal">
            Заказать звонок
          </button>
        </div>
        <!-- Modal -->
        <callModal>
          <h1>{{ сertificates }}</h1>
        </callModal>
      </div>
    </section>
  </div>
</template>

<script>

import $ from 'jquery'
import 'bootstrap';
import { Chart } from 'chart.js/auto'
import { get_certificates } from '@/api/certificates';
import callModal from '@/components/sendCallModal.vue';
export default {
  name: "HomeView",
  components: {callModal,
  },
  data(){
    return {
      certificates: []
    }
  },
  methods: {
    async photogalery() {
      // Sample array of image URLs
      var images = await get_certificates();
    
      // Populate gallery with images
      var gallery = $("#gallery");
      $.each(images, function (index, value) {
        gallery.append(`<div class="col-md-4 mb-3"><img src="${value}" class="img-fluid" data-index="${index}"></div>`);
      });

      // Lightbox functionality using Bootstrap modal
      gallery.on("mouseenter", "img", function () {
        $(this).css("cursor", "zoom-in");
      }).on("mouseleave", "img", function () {
        $(this).css("cursor", "default");
      }).on("click", "img", function () {
        var imgSrc = $(this).attr("src");
        var index = $(this).data("index");
        var modalHtml = `<div class="modal fade" id="photoModal" tabindex="-1" role="dialog" aria-labelledby="photoModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                    <div class="modal-body">
                                        <img src="${imgSrc}" class="img-fluid" data-index="${index}" style="cursor: zoom-out;">
                                    </div>
                                </div>
                            </div>
                        </div>`;
        $("body").append(modalHtml);
        window.$("#photoModal").modal("show");
        window.$("#photoModal").on("hidden.bs.modal", function () {
          window.$(this).remove();
        });
      });

      $("body").on("click", "#photoModal img", function () {
        var index = window.$(this).data("index");
        window.$(`#gallery img[data-index="${index}"]`).css("cursor", "zoom-in");
        window.$("#photoModal").modal("hide");
      });
    },

    chart() {

      var repairCanvas = document.getElementById("repairChart").getContext("2d");

      //В зависимости от размера экрана, ставим размер шрифта
      var size = window.innerWidth < 316 ? 5 : window.innerWidth < 355 ? 10 : window.innerWidth < 530 ? 12 : 16;

      // Данные для графика
      var repairData = {
        // Метки для оси X
        labels: ["Компьютеры", "Компьютерная техника", "Телефоны", "Планшеты", "Телевизоры", "Остальная техника"],
        datasets: [{
          label: "Отремонтированной техники (в %)",
          backgroundColor: "#198754",
          borderColor: "#198754",
          hoverBackgroundColor: "#13653F",
          data: [95, 96, 99, 97, 95, 98] // Данные по принесенной технике
        }]
      };

      // Создание графика
      new Chart(repairCanvas, {
        type: 'bar', // Тип графика
        data: repairData, // Данные для отображения
        response: true,
        options: {
          scales: {
            x: {
              // Настройки оси X
              ticks: {
                color: 'black', // Цвет меток
                font: {
                  size: size, // Размер шрифта
                  family: "Rubik" // Семейство шрифта
                }
              }
            },
            y: {
              // Настройки оси Y
              ticks: {
                color: 'black', // Цвет меток
                font: {
                  size: size, // Размер шрифта
                  family: 'Rubik' // Семейство шрифта
                }
              }
            }
          },
          plugins: {
            tooltip: {
              // Настройки всплывающей подсказки
              titleColor: 'white', // Цвет заголовка
              bodyColor: 'white', // Цвет текста
              bodyFont: {
                size: size, // Размер текста
                family: 'Rubik' // Семейство шрифта
              },
              titleFont: {
                size: size, // Размер заголовка
                family: 'Rubik' // Семейство шрифта
              },
              displayColors: false, // Отображение цветных квадратиков
            },
            legend: {
              display: false
            }
          },
          indexAxis: 'y', // Ось индексов (по оси Y)
          barPercentage: 1.0, // Процент ширины столбцов
        }
      })
    },
  },
  mounted() {
    this.chart();
    this.photogalery();
  },
  
}

</script>
<style scoped>
.heading {
  display: flex;
  align-items: center;
  margin: 16px 0;
}

.headingRight {
  margin-left: 16px;
  margin-bottom: 0;
}

.headingLeft {
  margin-right: 16px;
  margin-bottom: 0;
}

.text,
.heading {
  text-align: justify;
}

.text {
  font-size: 18px;
}

.HeadingText {
  margin: 16px 0;
  text-align: center;
}

.modal-content {
  background-color: rgba(255, 255, 255, 0) !important;
  border: none !important;
}

.orderCall {
  display: flex;
  justify-content: center;
}

.orderCall button {
  margin: 16px 0;
  padding: 1rem 5rem;
}

.window .modal-content {
  background-color: rgba(255, 255, 255) !important;
}

#errName,
#errPhone {
  color: red;
  opacity: 0;
  font-size: 12px;
  margin: 0;
}

/* Подвал */
footer {
  margin-top: 16px;
  padding: 16px 0;
  background-color: #F9F9F9;
}

footer .container {
  display: flex;
  justify-content: space-between;
}

#address {
  margin-top: 0;
}

footer p {
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  margin: 10px 0;
}

.link {
  color: black;
}

svg {
  margin-right: 15px;
}

.network {
  text-decoration: none;
}


.network>svg {
  transition: all 0.8s ease 0s;
}

.network>svg:hover {
  transform: scale(1.2);
}

iframe {
  width: 100%;
  height: 100%;
}

.modal-dialog-centered .modal-body {
  align-items: center;
}

@media (min-width: 992px) {
  .menu {
    width: 100%;
    position: fixed;
    z-index: 10;
  }

  .map {
    height: 500px;
    width: 500px;
  }

  .headingImg {
    width: 90%;
  }

  .iphoneImg {
    width: 40%;
  }

  .map {
    height: 500px;
    width: 500px;
  }

}

@media (max-width: 992px) {

  .dropdown-item {
    color: white !important;
  }

  .dropdown-menu {
    background-color: #0d6efd !important;
    border: none !important;
  }

  .menu {
    position: relative;
  }

  .headingImg {
    width: 50%;
  }

  .iphoneImg {
    width: 30%;
  }

  .map {
    height: 300px;
    width: 300px;
  }
}

@media (max-width: 768px) {
  .heading {
    flex-direction: column;
  }

  .headingImg {
    width: 70%;
  }

  .head2 {
    flex-direction: column-reverse;
  }

  .headingImg {
    margin: 16px 0;
  }

  .img-fluid {
    width: 70%;
  }

  .col-md-4 {
    display: flex;
    justify-content: center;
  }

  .modal-body {
    display: flex;
    justify-content: center;
  }

  .modal-dialog .modal-body {
    flex-direction: column;
  }

  .textSlide {
    display: none;
  }

  h5 {
    display: block !important;
  }

  .btn {
    width: 100%;
  }

  .container {
    flex-direction: column-reverse;
  }

  .map {
    margin-bottom: 16px;
    width: 100%;
  }
}

@media (min-width: 768px) {

  .modal-dialog-centered .modal-body img {
    width: 90%;
  }

  .modal-body {
    display: flex;
    flex-direction: column;
  }
}

@media (max-width: 576px) {

  .btn {
    width: 100%;
  }

}

@media (min-width: 1000px) {
  .modal-dialog-centered .modal-body img {
    width: 100%;
  }
}
</style>
