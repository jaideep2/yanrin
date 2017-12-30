-- noinspection SqlNoDataSourceInspectionForFile
BEGIN ISOLATION LEVEL READ COMMITTED;
-- News Table
CREATE TABLE news (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    publication TEXT NOT NULL,
    author TEXT NOT NULL,
    url TEXT NOT NULL,
    date DATE NOT NULL,
    year SMALLINT NOT NULL,
    month SMALLINT NOT NULL,
    content CHARACTER VARYING NOT NULL,
    rank REAL NOT NULL
);

-- CREATE INDEX alerts_user_id_index ON alerts(user_id);
COMMENT ON TABLE news IS 'Table for storing raw news data';
COMMENT ON COLUMN news.title IS 'News headline';
COMMENT ON COLUMN news.publication IS 'Name of publication';
COMMENT ON COLUMN news.author IS 'Author of article';
COMMENT ON COLUMN news.url IS 'News article link';
COMMENT ON COLUMN news.date IS 'Full date news article was published';
COMMENT ON COLUMN news.year IS 'Year news article was published';
COMMENT ON COLUMN news.month IS 'Month news article was published';
COMMENT ON COLUMN news.content IS 'Actual text of the article';
COMMENT ON COLUMN news.rank IS 'NewsRank between 1-10. 0 means not assigned yet';

-- Topics Table
CREATE TABLE topics (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL, --people, organization or location
    startdate DATE NOT NULL,
    enddate DATE NOT NULL,
    news_ids BIGINT[] NOT NULL
);

-- CREATE INDEX alerts_user_id_index ON alerts(user_id);
COMMENT ON TABLE topics IS 'Table for storing topic modeling data';
COMMENT ON COLUMN topics.name IS 'Topic name (not unique)';
COMMENT ON COLUMN topics.type IS 'Type of topic e.g. Person, location, country etc.';
COMMENT ON COLUMN topics.startdate IS 'Topic start date';
COMMENT ON COLUMN topics.enddate IS 'Topic end date';
COMMENT ON COLUMN topics.news_ids IS 'List of news ids in this topic';

-- Summary Table
CREATE TABLE summary (
    id BIGSERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    title TEXT NOT NULL,
    startdate DATE NOT NULL,
    enddate DATE NOT NULL,
    topic_ids BIGINT[] NOT NULL
);

-- CREATE INDEX alerts_user_id_index ON alerts(user_id);
COMMENT ON TABLE summary IS 'Table for storing summarization data';
COMMENT ON COLUMN summary.text IS 'Summary text';
COMMENT ON COLUMN summary.title IS 'Summary headline';
COMMENT ON COLUMN summary.startdate IS 'Summary start date';
COMMENT ON COLUMN summary.enddate IS 'Summary end date';
COMMENT ON COLUMN summary.topic_ids IS 'List of topic ids in this summary';

COMMIT;