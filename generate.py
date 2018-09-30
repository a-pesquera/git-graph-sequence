import os
import os.path
import base64
from selenium import webdriver


FINAL_DIR = 'images'
SENTENCES_JS = 'sentences.js'
IMG_FILE_TEMPLATE = 'image_{:02}.png'


def export_canvas(driver, canvas_id, file):
    canvas = driver.find_element_by_css_selector(canvas_id)
    get_canvas_script = "return arguments[0].toDataURL('image/png').substring(21);"
    canvas_base64 = driver.execute_script(get_canvas_script, canvas)
    canvas_png = base64.b64decode(canvas_base64)
    with open(file, 'wb') as f:
        f.write(canvas_png)


def main():
    driver = webdriver.Firefox()

    this_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(this_dir, FINAL_DIR)
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    driver.get(os.path.join('file://' + this_dir, 'selenium.html'))

    sentences_filename = os.path.join(this_dir, SENTENCES_JS)
    with open(sentences_filename) as f:
        lines = [l.strip() for l in f.readlines()]
        lines = [l for l in lines if l]

    for i, js_sentence in enumerate(lines, 1):
        driver.execute_script(js_sentence)
        img_file = os.path.join(FINAL_DIR, IMG_FILE_TEMPLATE.format(i))
        export_canvas(driver, '#gitGraph', img_file)

    driver.quit()


if __name__ == '__main__':
    main()
