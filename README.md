# skyscrappers-solver
Python program, that soves skyscrappers puzzle
# Usage
Запустите skyscrappers solver.exe 
(Вы также можете запустить src.py (требуется pyhon3) так: ```python src.py``` или ```python3 src.py```)
Далее введите ограничения пазла начиная с левого верхнего угла по часовой стрелке без разделителей, если ограничение отсутвует используйте 0.


![как правильно вводить ограничения](https://s113vla.storage.yandex.net/rdisk/efee134d0d335e4e8d2e35222956452012fa08fe6a4b62a358fd6c819f8102a6/5d5da615/9CCpEBR1IiRTaodlPB9NllrlHNYzgc6eaR58Zh4tJeQe7hxidGtHSF-LZmHlxlCWvr4N4_LcC99jx0OXCvEyng==?uid=0&filename=1.png&disposition=attachment&hash=qWn52gxVowCGUWrugCAIyBftzZDd5JtK75qyqXW36qwfxzhzigZKlLKD11/Stx4uq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=image%2Fpng&owner_uid=914594029&fsize=14550&hid=09e082d20e946d39dd17ec753294e5b6&media_type=image&tknv=v2&rtoken=3mE4nukkaZA4&force_default=no&ycrid=na-210cf715a79c2d1ce18cc932ee7af5e7-downloader19e&ts=590a63775ef40&s=eac7d3fe1c384bfe75efe55ae3749dc3bde88bd6405d4c6541a60d1a52c62ae4&pb=U2FsdGVkX19hopbbSNAGHPTKXnUWTuTIXss052YlG8bRerVM1xMe6GYW7colXe7vGPrA6m9vyBaXTHRDb_1XY-CEwy7_LSpZYrS-IB0-C-s)


Если в вашем пазле есть известные цифры вы сможете ввести их далее. Вводить нужно в следующем формате:
{строка}{столбец}{число} отсчет индекса столбца и строки начинается с 0. Нажмите ENTER после каждой тройки чисел. чтобы закончить ввод просто нажмите ENTER еще раз.

## Usage example
Опробуем на примере

![Пример задачи](https://downloader.disk.yandex.ru/preview/9bb448c56524ff48d846c7f7d61ab5ea378443a26ca6bdf95ab40dafa6ab5608/5d5ddb1b/VW5-f4U1tM6pElYoELXu1nU1RSSSCCh_lqi7ggpWDI2E3euNFpQOT3R0Us9LSxDeT3z0zor_p9XyTTeIyvTMMg%3D%3D?uid=0&amp;filename=2.png&amp;disposition=inline&amp;hash=&amp;limit=0&amp;content_type=image%2Fpng&amp;owner_uid=0&amp;tknv=v2&amp;size=2048x2048)

Запускаем skyscrappers solver.exe и вводим ограничения, как показано на рисунке. 
Должно получиться `30133000002030020300`
Нажимаем `ENTER`. Далее нужно ввести единичку, которая находится на самом поле.
вводим как в сказано в разделе "Usage".
Получится `211` (2 - индекс строки, 1 - индекс столбца, 1 - значение)
После ввода чисел появится начальное поле, оно должно соответствовать примеру (на месте пропусков 0).
