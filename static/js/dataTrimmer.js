const dataTrimmer = (HTMLData) => {
  /* ChannelUrl */
  const info =
    HTMLData.videoRenderer?.channelThumbnailSupportedRenderers
      .channelThumbnailWithLinkRenderer;
  const channelId = info?.navigationEndpoint.canonicalBaseUrl;
  const channelUrl = `https://www.youtube.com/${channelId}`;

  /* thumbnail */
  const thumbnailData = HTMLData.videoRenderer?.thumbnail?.thumbnails[0];
  const thumbnail = thumbnailData?.url;

  //유튜브 쇼츠인 경우, 이미지 크기 맞추기 힘듦. 썸네일 세로>가로면 버리기.
  if (!thumbnailData) return;
  const { height, width } = thumbnailData;
  if (height > width) return;

  /* Title */
  const titleData =
    HTMLData.videoRenderer?.title.accessibility.accessibilityData.label;

  /* Local용 */
  const titleLocalRegex = /^.*? (?=게시자: )/g;
  const title = titleLocalRegex.exec(titleData);

  /* ID */
  const id = HTMLData.videoRenderer?.videoId;
  const owner = HTMLData.videoRenderer?.ownerText.runs[0].text;
  const duration =
    HTMLData.videoRenderer?.lengthText?.accessibility?.accessibilityData.label;

  return {
    title: title ? title[0] : 'Not Found',
    id,
    channelUrl,
    thumbnail,
    duration,
    owner,
  };
};
