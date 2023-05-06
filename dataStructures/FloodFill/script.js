var floodFill = function (image, sr, sc, color) {
  if (image[sr][sc] == color) return image;

  const fill = (image, sr, sc, oldColor, color) => {
    if (
      sr < 0 ||
      sc < 0 ||
      sr >= image.length ||
      sc >= image[0].length ||
      image[sr][sc] != oldColor
    )
      return;

    image[sr][sc] = color;
    fill(image, sr + 1, sc, oldColor, color);
    fill(image, sr - 1, sc, oldColor, color);
    fill(image, sr, sc + 1, oldColor, color);
    fill(image, sr, sc - 1, oldColor, color);
  };

  fill(image, sr, sc, image[sr][sc], color);
  return image;
};
