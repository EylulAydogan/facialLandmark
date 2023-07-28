Bilgisayar mühendisliğinde gelişmeler 4 dersi bütünleme ödevidir.
Face landmarksa point cloud giydirilip göz içi çukur noktaları bulunmaya çalışılmıştır.
Python dili ile yazılmıştır. OpenCV, dlib, numpy, wavefront ve OpenGL kütüphaneleri kullanılmıştır.
Pycharm üzerine yazdım. opencv, numpy, wavefront ve opengl kendi uygulaması üzerinden indirilebildi ama dlib indirilmedi.
Dlib kütüphanesini internetten ayrıca dosya olarak indirip kullandım.


Kodu satır satır inceleyeceğim:
2. `cv2'yi içe aktar' - Görüntü işleme görevleri için kullanılan OpenCV kitaplığını içe aktarır.
3. "dlib'i içe aktar" - Yüz tanıma ve yer işaretleri algılaması sağlayan dlib kitaplığını içe aktarır.
5. `numpy'yi np olarak içe aktar' - Büyük, çok boyutlu diziler ve matrisler için destek sağlayan numpy kitaplığını içe aktarır.
6. "pywavefront import wavefront'tan" - wavefront (.obj) 3B modelleriyle çalışmak için kullanılan pywavefront kitaplığından wavefront modülünü içe aktarır.
7. `opengl.gl'den import *` - OpenGL kullanarak grafik işlemek için OpenGL kitaplığını içe aktarır.
8.`opengl.glut içe aktarmadan *` - Pencere oluşturma ve kullanıcı girdisini işleme desteği sağlayan GLUT kitaplığını içe aktarır.
9. `opengl.glu içe aktarmadan *` - OpenGL işlemleri için yardımcı işlevler sağlayan GLU kitaplığını içe aktarır. Sonraki satırlar, her içe aktarma veya modülün ne yaptığını açıklayan açıklamalardır. 
14. `detector = dlib.get_frontal_face_detector()` - dlib kitaplığını kullanarak bir yüz dedektörü nesnesi oluşturur.
15. `predictor = dlib.shape_predictor("FacialLandmark.png') - dlib'den shape_predictor() işlevini kullanarak yüz yer işaretleri tahmin modelini yükler.

18. `face_template_path = "kafa1.dxf"' - 3D yüz şablon dosyasının yolunu belirtir.
22-29."find_eye_center()" işlevi yüzdeki yer işaretlerini girdi olarak alır ve sol ve sağ gözlerin merkez noktalarını hesaplar.
31-46. "dress_face_template()" işlevi yüzdeki yer işaretlerini girdi olarak alır,
    "find_eye_center()" işlevini kullanarak göz merkezlerini bulur ve ardından OpenGL kullanarak 3D yüz şablonunu yüze giydirir.
48- 75. "process_face_landmarks()" işlevi, görüntü yolunu ve yüz şablonu yolunu girdi olarak alır.
    Görüntüyü OpenCV kullanarak okur, gri tonlamaya dönüştürür ve dlib yüz dedektörünü kullanarak yüzleri algılar.
    Yüzler algılanırsa, şekil öngörücüyü kullanarak yer işaretlerini çıkarır ve 3D yüz şablonunu yüze giydirmek için "dress_face_template()" işlevini çağırır.
    Son olarak, görüntüyü OpenCV kullanarak giyinmiş yüz şablonuyla görüntüler.
78-81.Sondaki kod bloğu, komut dosyasının doğrudan çalıştırılıp çalıştırılmadığını kontrol eder (modül olarak içe aktarılmaz).
      Görüntü yolunu ve yüz şablonu yolunu belirtir, ardından bu girişlerle "process_face_landmarks()" işlevini çağırır.

![3D-facial-landmark-detection-scheme-in-our-framework-A-The-coarse-facial-landmark](https://github.com/EylulAydogan/facialLandmark/assets/102043836/e2929fa9-d9c9-4735-b264-186c2a930c9f)
![FacialLandmarks1](https://github.com/EylulAydogan/facialLandmark/assets/102043836/bd1e462b-cc1a-405a-be38-c095ca7d4725)
![png-transparent-nose-face-polygon-mesh-3d-modeling-three-dimensional-space-nose-template-3d-computer-graphics-people](https://github.com/EylulAydogan/facialLandmark/assets/102043836/1b1df574-adfa-4aae-a501-076844fbe9d1)





