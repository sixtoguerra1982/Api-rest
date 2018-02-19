class CreateFeeds < ActiveRecord::Migration[5.1]
  def change
    create_table :feeds do |t|
      t.date :date_feed
      t.string :title
      t.string :image
      t.text :content
      t.text :all_content
      t.string :category
      t.timestamps
    end
  end
end
