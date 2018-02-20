class CreateLikes < ActiveRecord::Migration[5.1]
  def change
    create_table :likes do |t|
      t.integer :user_id
      t.boolean :like
      t.timestamps
    end
    add_reference :likes, :feed, index: true
  end
end
