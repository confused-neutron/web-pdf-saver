# User editable values
doc = 'bookname'
num_pages = 20


import time
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
from fpdf import FPDF


def get_page():
	return np.array(pyautogui.screenshot())[155*2:805*2, 465*2:975*2, :]

def flip_page():
	pyautogui.click(765, 790)

# Main method (takes a while to run)
def main():
	time.sleep(2)
	pdf = None

	for pg_num in range(num_pages):
		print('On page', str(pg_num + 1))
		page = get_page()
		plt.imsave('./' + doc + '/page_' + str(pg_num) + '.png', page)
		if pg_num == 0:
			height, width, _ = page.shape
			pdf = FPDF(unit = "pt", format = [width, height])
		pdf.add_page()
		time.sleep(0.1)
		pdf.image('./' + doc + '/page_' + str(pg_num) + '.png', 0, 0)
		flip_page()

	pdf.output('./' + doc + '/' + doc + '.pdf', 'F')

if __name__ == '__main__':
	main() 