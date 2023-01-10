const dataTrimmer = (data) => {
  /* ChannelUrl */
  const info =
    axiosData.videoRenderer?.channelThumbnailSupportedRenderers
      .channelThumbnailWithLinkRenderer;
  const channelId = info?.navigationEndpoint.canonicalBaseUrl;
  const channelUrl = `https://www.youtube.com/${channelId}`;

  /* thumbnail */
  const thumbnailData = axiosData.videoRenderer?.thumbnail?.thumbnails[0];
  const thumbnail = thumbnailData?.url;

  //유튜브 쇼츠인 경우, 이미지 크기 맞추기 힘듦. 썸네일 세로>가로면 버리기.
  if (!thumbnailData) return;
  const { height, width } = thumbnailData;
  if (height > width) return;

  /* Title */
  const titleData =
    axiosData.videoRenderer?.title.accessibility.accessibilityData.label;

  //axios가 받아오는 데이터 형식이 local, vercel에 따라 다름. (title에 정규표현식 안먹음!)
  /* Local용 */
  const titleLocalRegex = /^.*? (?=게시자: )/g; //텍스트의 처음부터 "게시자"의 전방탐색까지.
  const title = titleLocalRegex.exec(titleData);

  /* ID */
  const id = axiosData.videoRenderer?.videoId;

  const owner = axiosData.videoRenderer?.ownerText.runs[0].text;

  const duration =
    axiosData.videoRenderer?.lengthText?.accessibility?.accessibilityData.label;

  return {
    title: title ? title[0] : 'Not Found',
    id,
    channelUrl,
    thumbnail,
    duration,
    owner,
  };
};
