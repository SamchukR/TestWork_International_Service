# TestWork_International_Service
# Задание:
Реализовать тривиальное HTTP "Hello, world!" web-приложение на любом
удобном Вам языке программирования и завернуть его в clound native
окружение.

Требования:
  - Dockerfile, который докеризует приложение.
  - Приложение должно иметь health-check и ready-check.
  - Приложение должно предоставлять metrics endpoint для Prometheus
(метрики - на Ваше усмотрение).
  - Grafana dashboard с визуализацией метрик.
  - docker-compose.yml, который запускает приложение со всем необходимым
окружением (Prometheus и Grafana).

Временем и инструментом для выполнение тестового задания Вы не
ограничены. Любые другие аспекты реализации, которые не указаны в
требованиях, могут быть выполнены на Ваше усмотрение.

Следующее будет плюсом:
  - Kubernetes спеки приложения, либо Helm-чарт, для запуска его в
Minikube (в дополнение к docker-compose.yaml).
  - E2E-тесты, которые проверяют корректность докеризации приложения.
# Было реализовано следующее:
Было создано приложение с помощью Pyhton и библиотеки flask, реализующее простой web интерфейс с выводом Hello World!
Health-check был реализован с помощью одноименной библиотеки и расположен по адресу <<ip сервера с приложением>>/healthcheck
Метрики собираются с помощью библиотеки PrometheusMetrics и расположены по адресу <<ip сервера с приложением>>/metrics
Был написен docker-compose файл, который докеризирует приложение и окружение с сервисами Grafana и Prometheus, которые в связке предоставляют визуализацию метрик приложения, порты сервисов Grafana и Prometheus стандартные (3000 и 9090 соответвенно)
Запуск проекта осуществялется запуском docker-compose файла, в ходе которого запускаются и настраиваются 3 контейнера с необходимыми сервисами (docker-compose up -d --build)
