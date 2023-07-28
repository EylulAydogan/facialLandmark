# Öncelikle kütüphanelerle başlıyorum
import cv2 # Görüntü işleme görevleri için kullanılan OpenCV kitaplığını içe aktarır
import dlib # Yüz tanıma ve yer işaretleri algılaması sağlayan dlib kitaplığını içe aktarır
# dlib kütüphanesini internetten dosya olarak indirip buraya tanımladım
import numpy as np # Büyük, çok boyutlu diziler ve matrisler için destek sağlayan numpy kitaplığını içe aktarır
from pywavefront import wavefront # wavefront (.obj) 3D modelleriyle çalışmak için kullanılan pywavefront kitaplığından wavefront modülünü içe aktarır
from OpenGL.GL import * # OpenGL kullanarak grafik işlemek için OpenGL kitaplığını içe aktarır
from OpenGL.GLUT import * # Pencere oluşturma ve kullanıcı girdisini işleme desteği sağlayan GLUT kitaplığını içe aktarır
from OpenGL.GLU import * # OpenGL işlemleri için yardımcı işlevler sağlayan GLU kitaplığını içe aktarır. Sonraki satırlar, her içe aktarma veya modülün ne yaptığını açıklayan açıklamalardır



# Yüz landmarks noktalarını bulmak için dlib yüz tanıma modelini yükle
detector = dlib.get_frontal_face_detector()  # dlib kitaplığını kullanarak bir yüz dedektörü nesnesi oluşturur
predictor = dlib.shape_predictor("FacialLandmarks.png") # dlib'den shape_predictor() işlevini kullanarak yüz yer işaretleri tahmin modelini yükler

# Yüz şablonunu yükle
face_template_path = "Kafa1.dxf" # 3D yüz şablon dosyasının yolunu belirtir
face_template_mesh = wavefront(face_template_path)

# Nokta bulutunu işlemek ve yüz şablonunu giydirmek için fonksiyonlar
def find_eye_center(landmarks):  # find_eye_center()" işlevi yüzdeki yer işaretlerini girdi olarak alır ve sol ve sağ gözlerin merkez noktalarını hesaplar
    left_eye_landmarks = landmarks[36:42]
    right_eye_landmarks = landmarks[42:48]

    left_eye_center = np.mean(left_eye_landmarks, axis=0)
    right_eye_center = np.mean(right_eye_landmarks, axis=0)

    return left_eye_center, right_eye_center

def dress_face_template(landmarks):
    # "dress_face_template()" işlevi yüzdeki yer işaretlerini girdi olarak alır,
    # "find_eye_center()" işlevini kullanarak göz merkezlerini bulur ve ardından OpenGL kullanarak 3D yüz şablonunu yüze giydirir
    h, w = 100, 100  # Yüz şablonu boyutları - Ayarlayabilirsiniz

    left_eye_center, right_eye_center = find_eye_center(landmarks)
    x1, y1 = left_eye_center[0], left_eye_center[1]
    x2, y2 = right_eye_center[0], right_eye_center[1]

    glLoadIdentity()
    glTranslatef(x1 - w / 2, y1 - h / 2, 0.0)
    glBegin(GL_TRIANGLES)
    for face in face_template_mesh.faces:
        for vertex_id in face:
            glVertex3f(*face_template_mesh.vertices[vertex_id - 1])
    glEnd()

def process_face_landmarks(image_path, face_template_path):
    #"process_face_landmarks()" işlevi, görüntü yolunu ve yüz şablonu yolunu girdi olarak alır.
    # Görüntüyü OpenCV kullanarak okur, gri tonlamaya dönüştürür ve dlib yüz dedektörünü kullanarak yüzleri algılar.
    # Yüzler algılanırsa, şekil öngörücüyü kullanarak yer işaretlerini çıkarır ve 3D yüz şablonunu yüze giydirmek için "dress_face_template()" işlevini çağırır. Son olarak, görüntüyü OpenCV kullanarak giyinmiş yüz şablonuyla görüntüler
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = detector(gray_image)

    if len(faces) > 0:
        face = faces[0]
        landmarks = predictor(gray_image, face)

        landmark_points = []
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmark_points.append([x, y])

        landmark_points = np.array(landmark_points)

        # Yüz şablonunu giydirmek için yeni fonksiyon çağır
        dress_face_template(landmark_points)


    cv2.imshow("Yüz Şablonu ile Yüz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "3d-facial-landmark.png"
    face_template_path = "Kafa1.stl"  
    process_face_landmarks(image_path, face_template_path)

    # Sondaki kod bloğu, komut dosyasının doğrudan çalıştırılıp çalıştırılmadığını kontrol eder (modül olarak içe aktarılmaz).
    # Görüntü yolunu ve yüz şablonu yolunu belirtir, ardından bu girişlerle "process_face_landmarks()" işlevini çağırır