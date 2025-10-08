import numpy as np

def template_match(image, template):
    h_img, w_img = image.shape
    h_temp, w_temp = template.shape

    best_score = float('inf')
    best_loc = (0, 0)

    for y in range(h_img - h_temp):
        for x in range(w_img - w_temp):
            patch = image[y:y+h_temp, x:x+w_temp]
            diff = np.sum((patch - template)**2)
            if diff < best_score:
                best_score = diff
                best_loc = (x, y)

    return best_loc, best_score

image = np.array([
    [10,20,20,20,10,10],
    [10,20,50,20,10,10],
    [10,20,20,20,10,10],
    [10,10,10,10,10,10],
    [10,10,10,10,10,10],
])

template = np.array([
    [20,20,20],
    [20,50,20],
    [20,20,20],
])

loc, score = template_match(image, template)
print("Best match location:", loc)
print("Matching score:", score)

def iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    return interArea / float(boxAArea + boxBArea - interArea)

gt_box = (1,1,3,3)
pred_box = (1,1,3,3)
print("IoU:", iou(gt_box, pred_box))
