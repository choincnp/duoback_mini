const musicDataParser = (HTMLData) => {
  const regex = /(var ytInitialData)(.*?)};/;
  const parsedRegexHTML = regex.exec(HTMLData);
  const CSRData = parsedRegexHTML[0];
  const objectData = JSON.parse(CSRData.substring(20, CSRData.length - 1));
  const returnData =
    objectData.contents.twoColumnSearchResultsRenderer.primaryContents
      .sectionListRenderer?.contents[0].itemSectionRenderer.contents;

  const filteredData = returnData
    .map((data) => dataTrimmer(data))
    .filter((data) => {
      if (!data) return false;
      for (const item in data) {
        if (!item) return false;
      }

      return true;
    });

  return filteredData;
};
