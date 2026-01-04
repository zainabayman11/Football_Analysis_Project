def get_center_of_bbox(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int((y1+y2)/2) 
# # 📌 Gets the center of the body
# Used for:
# - The ball
# - Determining the player's horizontal position


def get_bbox_width(bbox):
    return bbox[2]-bbox[0]

# 📌 Player width # ✔ Important for: # - Drawing an ellipse under the player # - Estimating his size in the image


def measure_distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def measure_xy_distance(p1,p2):
    return p1[0]-p2[0],p1[1]-p2[1]

# 📌 Gets the foot position on the ground # Why? # The player's real position is calculated from his foot, not his head # This is more accurate for: # - Distances # - Speed # - Ball possession
def get_foot_position(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int(y2)