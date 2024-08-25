# pytestAT03
 Мокирование и тестирование API

✅ Мокирование (mocking) — это техника в тестировании, позволяющая имитировать поведение реальных объектов. Это полезно, когда необходимо тестировать компоненты системы, зависящие от внешних сервисов, API или сложных объектов, которые трудно или невозможно использовать напрямую в тестах.

При создании программ они часто взаимодействуют с другими частями системы или внешними сервисами, такими как API, базы данных и так далее. При тестировании мы должны быть уверены, что наша программа работает правильно, даже если внешние сервисы недоступны или работают нестабильно. Мокирование позволяет нам притвориться, что внешние сервисы работают так, как нам нужно, даже если это не так. Мы как бы создаем фальшивый сервис, который возвращает предопределенные ответы, которые мы сами задаем, и эти ответы используем в нашей программе.



Преимущества мокирования:

Изоляция тестов. Мокирование позволяет изолировать тестируемый код от внешних зависимостей, полностью контролируя все, что происходит.
Контроль над окружением. Мы можем точно контролировать данные, возвращаемые mock-объектом, что облегчает тестирование различных сценариев.
Повышение производительности. Тесты с использованием мокирования выполняются быстрее, так как не требуется доступ к реальным сервисам.
Надежность. Тесты не зависят от доступности внешних сервисов или состояния сети, что позволяет им работать стабильно.
Основные понятия в мокировании

✅ Mock-объект — объект, имитирующий поведение реального объекта или сервиса.

✅ Patch — изменение поведения функции или объекта во время выполнения теста.

✅ Spy — объект, записывающий информацию о вызовах, методах и параметрах.

✅Stub — реализация интерфейса, возвращающая предопределенные данные.
